<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'vendor/PHPMailer-master/src/PHPMailer.php';
require 'vendor/PHPMailer-master/src/SMTP.php';
require 'vendor/PHPMailer-master/src/Exception.php';

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
    // Captura los datos del formulario y sanitiza
    $email = htmlspecialchars($_POST['email']);
    $firstName = htmlspecialchars($_POST['firstName']);
    $lastName = htmlspecialchars($_POST['lastName']);
    $companyName = htmlspecialchars($_POST['companyName']);
    $help = htmlspecialchars($_POST['help']);
    $additionalDetails = htmlspecialchars($_POST['additionalDetails']);
    // Captura los valores de los checkboxes (si están marcados)
    $receiveCommunications = isset($_POST['receiveCommunications']) ? 'Yes' : 'No';
    $allowPersonalData = isset($_POST['allowPersonalData']) ? 'Yes' : 'No';

    // Construye el mensaje del correo
    $to = "info@ravencorex.com"; // Destinatario
    $subject = "New Contact Form Submission";
    $body = "
        <h2>New Contact Form Submission</h2>
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