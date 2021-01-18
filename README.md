
## dnmp


> docker + nginx + mysql + php（5.6、7.2、7.3）+ redis + mongo



本环境基于[docker-lnmp-with-mutli-php-versions](https://github.com/c0priwolf/docker-lnmp-with-mutli-php-versions)完成。

部分地方修改了下适合自己测试。


## 文件目录

```
.
├── build               镜像构建目录
│   └── php
│       ├── php56
│       ├── php72
│       └── php73
├── config              配置文件目录
│   ├── mongo           
│   ├── mysql
│   │   ├── mysql5
│   │   └── mysql8
│   ├── nginx
│   │   ├── conf.d
│   │   └── nginx.conf
│   ├── php
│   │   ├── php56
│   │   ├── php72
│   │   └── php73
│   └── redis
├── data                数据目录
│   ├── composer
│   └── mysql           mysql log也在这个路径
├── docker-compose.yml  docker-compose
├── logs                日志文件目录
│   ├── nginx
│   ├── php-fpm
│   └── xdebug
├── MySQL-Monitor.py    mysql日志监控
└── site                网站目录


```


## 参考
- [c0priwolf/docker-lnmp-with-mutli-php-versions](https://github.com/c0priwolf/docker-lnmp-with-mutli-php-versions)
- [yeszao/dnmp](https://github.com/yeszao/dnmp)
- [micooz/docker-lnmp](https://github.com/micooz/docker-lnmp)
- [dnmp-plus](https://www.guanguans.cn/dnmp-plus/)