<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'vendor/PHPMailer-master/src/PHPMailer.php';
require 'vendor/PHPMailer-master/src/SMTP.php';
require 'vendor/PHPMailer-master/src/Exception.php';

// Anti-spam functions
function verifyRecaptcha($recaptchaResponse) {
    $configPath = __DIR__ . '/../u345824653/config.php';
    $config = require $configPath;
    
    $secretKey = $config['recaptcha_secret_key'];
    $url = 'https://www.google.com/recaptcha/api/siteverify';
    
    $data = array(
        'secret' => $secretKey,
        'response' => $recaptchaResponse,
        'remoteip' => $_SERVER['REMOTE_ADDR']
    );
    
    $options = array(
        'http' => array(
            'header' => "Content-type: application/x-www-form-urlencoded\r\n",
            'method' => 'POST',
            'content' => http_build_query($data)
        )
    );
    
    $context = stream_context_create($options);
    $result = file_get_contents($url, false, $context);
    $response = json_decode($result);
    
    return $response->success;
}

function isSpam($firstName, $lastName, $email, $additionalDetails) {
    // Check for suspicious patterns
    $spamPatterns = [
        '/^[A-Z]{10,}$/i', // All caps strings longer than 10 chars
        '/^[a-z]{10,}$/i', // All lowercase strings longer than 10 chars
        '/[A-Za-z]{15,}/', // Very long strings without spaces
        '/^[A-Z][a-z]*[A-Z][a-z]*[A-Z]/', // Mixed case patterns like "aGNLGYVdIKSEG"
    ];
    
    $fields = [$firstName, $lastName];
    
    foreach ($fields as $field) {
        foreach ($spamPatterns as $pattern) {
            if (preg_match($pattern, $field)) {
                return true;
            }
        }
    }
    
    // Check for suspicious email patterns
    $suspiciousEmails = [
        '/gmail\.com$/', // You can be more specific with known spam email patterns
        // Add more patterns as needed
    ];
    
    // Check if first/last name are too similar (random strings)
    if (strlen($firstName) > 8 && strlen($lastName) > 8) {
        $similarity = 0;
        similar_text($firstName, $lastName, $similarity);
        if ($similarity > 50) { // If names are too similar, likely spam
            return true;
        }
    }
    
    return false;
}

function logSpamAttempt($data) {
    $logFile = __DIR__ . '/spam_attempts.log';
    $timestamp = date('Y-m-d H:i:s');
    $ip = $_SERVER['REMOTE_ADDR'];
    $userAgent = $_SERVER['HTTP_USER_AGENT'] ?? 'Unknown';
    
    $logEntry = "[$timestamp] IP: $ip | User-Agent: $userAgent | Data: " . json_encode($data) . "\n";
    file_put_contents($logFile, $logEntry, FILE_APPEND | LOCK_EX);
}

function rateLimitCheck($ip) {
    $rateFile = __DIR__ . '/rate_limit.json';
    $maxAttempts = 5; // Max 5 submissions per hour
    $timeWindow = 3600; // 1 hour in seconds
    
    $rateData = [];
    if (file_exists($rateFile)) {
        $rateData = json_decode(file_get_contents($rateFile), true) ?: [];
    }
    
    $currentTime = time();
    
    // Clean old entries
    foreach ($rateData as $ipAddr => $attempts) {
        $rateData[$ipAddr] = array_filter($attempts, function($timestamp) use ($currentTime, $timeWindow) {
            return ($currentTime - $timestamp) < $timeWindow;
        });
        if (empty($rateData[$ipAddr])) {
            unset($rateData[$ipAddr]);
        }
    }
    
    // Check current IP
    if (!isset($rateData[$ip])) {
        $rateData[$ip] = [];
    }
    
    if (count($rateData[$ip]) >= $maxAttempts) {
        return false; // Rate limit exceeded
    }
    
    // Add current attempt
    $rateData[$ip][] = $currentTime;
    
    // Save rate data
    file_put_contents($rateFile, json_encode($rateData), LOCK_EX);
    
    return true; // Rate limit OK
}

function sendEmail($to, $subject, $body) {
    $mail = new PHPMailer(true);

    try {
        // Configuración del servidor SMTP de Google Workspace
        
        $mail->isSMTP();
        $mail->Host       = 'smtp.gmail.com';
        $mail->SMTPAuth   = true;
        
        $configPath = __DIR__ . '/../u345824653/config.php';
        
        $config = require $configPath;
        
        $mail->Username = $config['smtp_user'];
        $mail->Password = $config['smtp_pass'];
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port       = 587;

        // Configuración del correo
        $mail->setFrom('info@ravencorex.com', 'Ravencorex');
        $mail->addAddress($to);
        $mail->addReplyTo('info@ravencorex.com', 'Soporte Ravencorex');
        $mail->Subject = $subject;
        $mail->isHTML(true);
        $mail->Body    = $body;

        // Enviar correo
        $mail->send();
        return true;
    } catch (Exception $e) {
        return "Error al enviar el correo: {$mail->ErrorInfo}";
    }
}

// Enviar el correo desde el formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $ip = $_SERVER['REMOTE_ADDR'];
    
    // Rate limiting check
    if (!rateLimitCheck($ip)) {
        echo json_encode(['success' => false, 'message' => 'Too many submissions. Please try again later.']);
        exit;
    }
    
    // Verify reCAPTCHA
    $recaptchaResponse = $_POST['g-recaptcha-response'] ?? '';
    if (!verifyRecaptcha($recaptchaResponse)) {
        echo json_encode(['success' => false, 'message' => 'reCAPTCHA verification failed. Please try again.']);
        exit;
    }
    
    // Captura los datos del formulario y sanitiza
    $email = htmlspecialchars($_POST['email'] ?? '');
    $firstName = htmlspecialchars($_POST['firstName'] ?? '');
    $lastName = htmlspecialchars($_POST['lastName'] ?? '');
    $companyName = htmlspecialchars($_POST['companyName'] ?? '');
    $help = htmlspecialchars($_POST['help'] ?? '');
    $additionalDetails = htmlspecialchars($_POST['additionalDetails'] ?? '');
    
    // Validate required fields
    if (empty($email) || empty($firstName) || empty($lastName) || empty($help)) {
        echo json_encode(['success' => false, 'message' => 'Please fill in all required fields.']);
        exit;
    }
    
    // Check for spam patterns
    if (isSpam($firstName, $lastName, $email, $additionalDetails)) {
        // Log spam attempt
        logSpamAttempt([
            'ip' => $ip,
            'email' => $email,
            'firstName' => $firstName,
            'lastName' => $lastName,
            'companyName' => $companyName,
            'help' => $help,
            'additionalDetails' => $additionalDetails
        ]);
        
        // Return success to avoid alerting spammer, but don't send email
        echo json_encode(['success' => true, 'message' => 'Message sent successfully.']);
        exit;
    }
    
    // Captura los valores de los checkboxes (si están marcados)
    $receiveCommunications = isset($_POST['receiveCommunications']) ? 'Yes' : 'No';
    $allowPersonalData = isset($_POST['allowPersonalData']) ? 'Yes' : 'No';

    // Construye el mensaje del correo
    $to = "info@ravencorex.com"; // Destinatario
    $subject = "New Contact Form Submission";
    $body = "
        <h2>New Contact Form Submission</h2>
        <p><strong>IP Address:</strong> $ip</p>
        <p><strong>Email:</strong> $email</p>
        <p><strong>First Name:</strong> $firstName</p>
        <p><strong>Last Name:</strong> $lastName</p>
        <p><strong>Company Name:</strong> $companyName</p>
        <p><strong>Help Needed:</strong> $help</p>
        <p><strong>Additional Details:</strong> $additionalDetails</p>
        <p><strong>Receive Communications:</strong> $receiveCommunications</p>
        <p><strong>Consent to Store Personal Data:</strong> $allowPersonalData</p>

    ";

    // Enviar el correo
    $sendStatus = sendEmail($to, $subject, $body);

    
    if ($sendStatus === true) {
        echo json_encode(['success' => true, 'message' => 'Message sent successfully.']);
    } else {
        echo json_encode(['success' => false, 'message' => $sendStatus]);
    }
    
} else {
   // echo json_encode(['error' => false, 'message' => 'Invalid request method.']);
}
?>