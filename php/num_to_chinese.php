<?php
// 阿拉伯数字转中文
function num_to_chinese($num) {
    $digits = ['零','一','二','三','四','五','六','七','八','九'];
    $units = ['', '十', '百', '千', '万', '十', '百', '千', '亿'];
    $s = strval($num);
    $len = strlen($s);
    $result = '';
    for ($i = 0; $i < $len; $i++) {
        $d = intval($s[$i]);
        if ($d != 0) {
            $result .= $digits[$d] . $units[$len - 1 - $i];
        } else {
            if ($result && substr($result, -1) != '零') {
                $result .= '零';
            }
        }
    }
    return rtrim($result, '零');
}

$num = readline("输入数字: ");
echo "中文: " . num_to_chinese($num) . PHP_EOL;
