<?php
// Activar errores
ini_set('display_errors', 1);
error_reporting(E_ALL);

// Construir ruta
$configPath = __DIR__ . '/../u345824653/config.php';

// Verificar existencia
if (!file_exists($configPath)) {
    echo json_encode([
        'success' => false,
        'message' => 'El archivo config.php no fue encontrado en ' . $configPath
    ]);
    exit;
}

// Cargar configuración
$config = require $configPath;

// Validar contenido
if (!is_array($config)) {
    echo json_encode([
        'success' => false,
        'message' => 'config.php no devolvió un array válido'
    ]);
    exit;
}

if (!isset($config['smtp_user']) || !isset($config['smtp_pass'])) {
    echo json_encode([
        'success' => false,
        'message' => 'Faltan claves smtp_user o smtp_pass'
    ]);
    exit;
}

// Mostrar valores (por seguridad solo smtp_user)
echo json_encode([
    'success' => true,
    'smtp_user' => $config['smtp_user'],
    'smtp_pass_present' => !empty($config['smtp_pass']) // no imprimimos la clave real
]);