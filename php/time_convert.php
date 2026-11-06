<?php
// 时间转换器
function show_now() {
    echo "当前本地时间: " . date("Y-m-d H:i:s") . PHP_EOL;
    echo "当前时间戳:   " . time() . PHP_EOL;
}

function ts_to_time($ts) {
    return date("Y-m-d H:i:s", intval($ts));
}

function time_to_ts($date_str) {
    $dt = DateTime::createFromFormat("Y-m-d H:i:s", $date_str);
    return $dt ? $dt->getTimestamp() : "格式错误";
}

echo "=== 时间转换器 ===" . PHP_EOL;
show_now();
echo PHP_EOL;

$ts = readline("输入时间戳转时间（直接回车跳过）: ");
if (trim($ts)) {
    echo "转换结果: " . ts_to_time($ts) . PHP_EOL;
}

$ds = readline("输入时间转时间戳（YYYY-MM-DD HH:MM:SS）: ");
if (trim($ds)) {
    echo "转换结果: " . time_to_ts($ds) . PHP_EOL;
}
