<?php
// 大小写转换工具
$text = readline("输入英文: ");
echo "全大写: " . strtoupper($text) . PHP_EOL;
echo "全小写: " . strtolower($text) . PHP_EOL;
echo "首字母大写: " . ucwords($text) . PHP_EOL;
