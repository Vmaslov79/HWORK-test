<?php
while(true !==false){
    file_put_contents('service.log', date("Y-m-d h:i:s", time()).PHP_EOL ,FILE_APPEND);
    sleep(5);
}