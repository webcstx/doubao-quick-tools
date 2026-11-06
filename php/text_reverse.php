<?php
// 文本反转工具
function reverse_text($text) {
    return strrev($text);
}

$text = readline("输入要反转的文本: ");
echo "反转结果: " . reverse_text($text) . PHP_EOL;
