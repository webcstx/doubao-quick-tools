<?php
// Base64 编解码工具
function encode_b64($text) { return base64_encode($text); }
function decode_b64($text) { return base64_decode($text); }

$text = readline("输入要编码的文本: ");
echo "编码结果: " . encode_b64($text) . PHP_EOL;
$code = readline("输入要解码的Base64: ");
echo "解码结果: " . decode_b64($code) . PHP_EOL;
