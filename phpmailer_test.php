<?php
require 'vendor/autoload.php'; // Si usas Composer
// require 'path/to/PHPMailer.php'; // Si usas los archivos manualmente

use PHPMailer\PHPMailer\PHPMailer;

try {
    $mail = new PHPMailer();
    echo "PHPMailer is installed and working!";
} catch (Exception $e) {
    echo "PHPMailer is not installed or there's an error: " . $e->getMessage();
}
?>