#coding=utf-8
'''
Created on 2018-4-4

@author: Administrator
'''
import re
html = '''

<!DOCTYPE html>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=9; IE=8; IE=7; IE=EDGE">
<meta charset="UTF-8"/>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

<title>上海市第一中级人民法院 - 公拍网</title>

<META name=keywords content="公拍网,司法拍卖,上海拍卖行业也会,上海市公共资源拍卖中心,上海市网络拍卖公共平台，上海拍卖行，拍卖，拍卖行业，拍卖行业协会，行业协会" >
<meta http-equiv="x-dns-prefetch-control" content="on" />
<link rel="dns-prefetch" href="http://www.gpai.net" />
<link rel="stylesheet" type="text/css" href="/common/common.css" />
<link rel="stylesheet" type="text/css" href="css/style.css?v=201712" />
<link href="/plugin/bootstrap/bootstrap.min.css" rel="stylesheet" type="text/css">


<link rel="stylesheet" type="text/css" href="/plugin/bootstrap/bootstrap.min.css" />



<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?263a15f1b2e57ebc22960d3fa7c5537e";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
})();
</script>
</head>
<body>
<div class="container">
<!-- header -->
<div class="header">
    <div class="auto">
    <div class="top-left fl">
    <a href="http://www.gpai.net/">公拍网</a><span class="xian">|</span>
    <a href="http://www.gpai.net/sf/" >司法拍卖</a><span class="xian">|</span>
    <a href="http://www.gpai.net/bm/">司法变卖</a><span class="xian">|</span>
    <a href="http://www.gpai.net/zc/" >资产拍卖 <img src="/images/new.png"  height="13" border="0" alt=""></a><span class="xian">|</span>
    <a href="http://xj.gpai.net" >新疆分站</a><span class="xian">|</span>
    <!-- <a href="http://fe.gpai.net/" target="_blank">旧版入口 </a>
 -->    </div>
    <div class="top-right fr">

 
 <a href="https://www.gpai.net/user/login.do">登录</a><a>&nbsp;&nbsp;</a><a href="http://www.gpai.net/user/reg.do">注册</a>



    <span class="xian">|</span>
    <a href="http://www.gpai.net/user/">我的公拍网<i></i></a><span class="xian">|</span>
    <a href="#">微博<i></i></a><span class="xian">|</span>
    <a href="#">微信<i></i>
    <div class="top-down down-ewm">
    <img src="../images/ewm.png" alt="" />
    </div>
    </a><span class="xian">|</span>
    <a href="http://m.gpai.net/">手机站<i></i></a>
    </div>
    </div>
</div>
<!-- header End -->

    <div style="min-width:1190px;height: 130px;background: url('images/top2.jpg') no-repeat center rgb(164, 10, 3); margin-top: 30px;"></div>




<div class="header2">
 <div class="auto">
  <div class="header2-logo">
  <a href="http://www.gpai.net/"><img src="images/sf_logo.jpg" alt="" /></a>
  </div>
  <div class="header2-city"> 
  
 
  </div>
  <div class="header2-search">
  <div class="hot-keys">
   
  </div>
  <div class="header2-search2">
   <form action="http://s.gpai.net/sf/Search.do" method="get">
   <input type="text" placeholder="输入拍品关键词" name="q"  class="search2-int"/>
  <input type="submit" value="" class="search2-btn" title="搜索"  />
  </form>
  </div>
  <a href="http://s.gpai.net/sf/Search.do" class="gaoji-search">高级搜索</a>
  </div>
  <div class="sj-gpai">
  <img src="images/xq_code.png" alt="" width="75"/><br />
  手机逛公拍
  </div>
 </div>
</div>
<!-- 弹出地区 -->
<div id="fade" class="zsy-h3-h"></div>
<div class="zsy-h3-">
 <div id="light" class="zsy-h3">
  <h4>请选择城市<a href = "javascript:void(0)" onclick = "document.getElementById('light').style.display='none';document.getElementById('fade').style.display='none'"><img src="images/close.png" /></a></h4>
  <div class="zsy-h3-h4">
   <a id="zsy-h3-h4-a" href="#">上海</a>
   <a href="http://xj.gpai.net/">新疆</a>
   <a href="#"></a>
  </div>
 </div>
</div>
<!-- 弹出地区结束 -->
<div class="menu2">
<div class="auto">
    <li><a href="http://s.gpai.net/sf/notice.do">公告</a></li>
    <li><a href="http://s.gpai.net/sf/search.do">标的</a></li>
    <li><a href="http://s.gpai.net/sf/search.do?action=court">法院自主拍卖</a>（<a href="http://s.gpai.net/sf/search.do?action=selloff">变卖</a>）<i class='mhot'></i></li>
    <li><a href="http://www.gpai.net/sf/courtList.do">法院</a></li>
    
<li><a href="http://www.gpai.net/sf/partner.do">机构</a>

 </li>
<li><a href="http://www.gpai.net/sf/partner.do#block-col-wrap03">金融服务</a><i class='mhot'></i></li>
<li><a href="http://www.gpai.net/sf/LiveHall.do">直播</a></li>
<li><a href="http://www.gpai.net/sf/Help.do">帮助</a></li>

  <li class='pr10' style='float:right'><a href="http://www.gpai.net/sf/partnerWelcome.do">法院入驻<i class='mhot'></i></a>
  </li>
  </div>
</div>



            <!-- 内容部分 -->


            <!-- 7搜索2 -->
            <div class="block-wrap notice-wrap">
                <div class="auto">

                    <div class="searchtop">
<span class='searchtitle'>上海市第一中级人民法院</span><a href='court.do?id=1101'  class='searchlink'>标的&nbsp;（187）</a><a href='http://s.gpai.net/sf/notice.do?courtCode=1101'  class='searchlink2'>公告&nbsp;（219）</a>
                    </div>

                    <div class="type-select">

                        <div class="select-tab">
                            <div class="s-tab-l fl">
                                <span>标的类型</span>
                            </div>
                            <div class="s-tab-con">
<a href="http://www.gpai.net/sf/court.do?id=1101&restate=1&" class='bux'>不限</a><a href='http://www.gpai.net/sf/court.do?id=1101&restate=1&at=' class='selected'>房产</a><a href='http://www.gpai.net/sf/court.do?id=1101&restate=1&at=381'>土地</a><a href='http://www.gpai.net/sf/court.do?id=1101&restate=1&at=372'>股权</a><a href='http://www.gpai.net/sf/court.do?id=1101&restate=1&at=378'>机动车</a><a href='http://www.gpai.net/sf/court.do?id=1101&restate=1&at=383'>船舶</a><a href='http://www.gpai.net/sf/court.do?id=1101&restate=1&at=377'>物资</a><a href='http://www.gpai.net/sf/court.do?id=1101&restate=1&at=382'>财产性权益</a><a href='http://www.gpai.net/sf/court.do?id=1101&restate=1&at=379'>其他</a>

                            </div>
                        </div>
                        <div class="select-tab">
                            <div class="s-tab-l fl">
                                <span>价格区间</span>
                            </div>
                            <div class="s-tab-con">
<a href="http://www.gpai.net/sf/court.do?id=1101&at=376&restate=1&" class='selected bux'>不限</a><a href='http://www.gpai.net/sf/court.do?id=1101&at=376&restate=1&pr=441'>150万以下</a><a href='http://www.gpai.net/sf/court.do?id=1101&at=376&restate=1&pr=444'>150-300万</a><a href='http://www.gpai.net/sf/court.do?id=1101&at=376&restate=1&pr=445'>300-500万</a><a href='http://www.gpai.net/sf/court.do?id=1101&at=376&restate=1&pr=446'>500-1000万</a><a href='http://www.gpai.net/sf/court.do?id=1101&at=376&restate=1&pr=447'>1000万以上</a>
                            </div>
                        </div>

                        <div class="select-tab">
                            <div class="s-tab-l fl">
                                <span>拍卖状态</span>
                            </div>
                            <div class="s-tab-con"><a href="http://www.gpai.net/sf/court.do?id=1101&at=376&" class='bux'>不限</a><a href='http://www.gpai.net/sf/court.do?id=1101&at=376&restate=2'>正在拍卖</a><a href='http://www.gpai.net/sf/court.do?id=1101&at=376&restate=1' class='selected'>即将开始</a><a href='http://www.gpai.net/sf/court.do?id=1101&at=376&restate=3'>已成交</a><a href='http://www.gpai.net/sf/court.do?id=1101&at=376&restate=4'>其他</a></div>
                        </div>




                    </div>




                    <div class="sm-filtbar">
                        <div class="filtbar-l fl">
                            <span>
共有拍品（<label>16</label>）                            
                            
                            </span>
                        </div>
                        <div class="filtbar-con clearfix">

                        </div>
                    </div>
                    <div class="filt-result-list">
                        <ul class="main-col-list clearfix">


                            <li>
                                <div class="list-item"><span class="badge-arrow3">
在线拍
                                    </span><span class="badge-icon badge-bg103">即将开始
                                    </span>
                                    <a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=15822"><img src="http://imgcdn.gpai.net/upload/courtfile/2018-2/201802281508423547.jpg" alt="" /></a>
                                    <div class="item-tit"><a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=15822">上海市长宁区中山西路930号101、201、301室</a></div>
                                    <div class="gpai-infos">
                                        <p><p><span>起拍价：</span><b class='price-red'>76360000</b><span class='price-red'>元</span></p> </p>

                                            <p><span>评估价：</span> <span><b>10908.4</b>万元</span></p>
                                        <p><span>开始时间：2018-04-16 10:00:00</span> </p>
                                        <div class="m-infos-people clearfix">
                                            <span class="dif-line"></span>
                                            <div class="whalf fl">0 <span>次出价</span></div>
                                            <div class="whalf fr"><a href='http://www.gpai.net/sf\item2.do?Web_Item_ID=15822'>详细</a></div>
                                        </div>
                                    </div>
                                </div>
                            </li>


                            <li>
                                <div class="list-item"><span class="badge-arrow3">
在线拍
                                    </span><span class="badge-icon badge-bg103">即将开始
                                    </span>
                                    <a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=15929"><img src="http://imgcdn.gpai.net/upload/courtfile/2018-3/201803061127049785.jpg" alt="" /></a>
                                    <div class="item-tit"><a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=15929">上海市黄浦区中山南路200弄8号楼2702室及地下一层车位C89</a></div>
                                    <div class="gpai-infos">
                                        <p><p><span>起拍价：</span><b class='price-red'>19236000</b><span class='price-red'>元</span></p> </p>

                                            <p><span>评估价：</span> <span><b>2748</b>万元</span></p>
                                        <p><span>开始时间：2018-04-16 10:00:00</span> </p>
                                        <div class="m-infos-people clearfix">
                                            <span class="dif-line"></span>
                                            <div class="whalf fl">0 <span>次出价</span></div>
                                            <div class="whalf fr"><a href='http://www.gpai.net/sf\item2.do?Web_Item_ID=15929'>详细</a></div>
                                        </div>
                                    </div>
                                </div>
                            </li>


                            <li>
                                <div class="list-item"><span class="badge-arrow3">
在线拍
                                    </span><span class="badge-icon badge-bg103">即将开始
                                    </span>
                                    <a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=15972"><img src="http://imgcdn.gpai.net/upload/courtfile/2018-3/201803071358273740.jpg" alt="" /></a>
                                    <div class="item-tit"><a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=15972">上海市黄浦区泰康路190弄6号101室</a></div>
                                    <div class="gpai-infos">
                                        <p><p><span>起拍价：</span><b class='price-red'>6500000</b><span class='price-red'>元</span></p> </p>

                                            <p><span>评估价：</span> <span><b>926</b>万元</span></p>
                                        <p><span>开始时间：2018-04-16 10:00:00</span> </p>
                                        <div class="m-infos-people clearfix">
                                            <span class="dif-line"></span>
                                            <div class="whalf fl">0 <span>次出价</span></div>
                                            <div class="whalf fr"><a href='http://www.gpai.net/sf\item2.do?Web_Item_ID=15972'>详细</a></div>
                                        </div>
                                    </div>
                                </div>
                            </li>


                            <li>
                                <div class="list-item"><span class="badge-arrow3">
在线拍
                                    </span><span class="badge-icon badge-bg103">即将开始
                                    </span>
                                    <a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16064"><img src="http://imgcdn.gpai.net/upload/courtfile/2018-1/201801031102497335.jpg" alt="" /></a>
                                    <div class="item-tit"><a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16064">合肥市马鞍山南路新都会联邦花园5幢106室</a></div>
                                    <div class="gpai-infos">
                                        <p><p><span>起拍价：</span><b class='price-red'>1254400</b><span class='price-red'>元</span></p> </p>

                                            <p><span>评估价：</span> <span><b>224</b>万元</span></p>
                                        <p><span>开始时间：2018-04-16 10:00:00</span> </p>
                                        <div class="m-infos-people clearfix">
                                            <span class="dif-line"></span>
                                            <div class="whalf fl">0 <span>次出价</span></div>
                                            <div class="whalf fr"><a href='http://www.gpai.net/sf\item2.do?Web_Item_ID=16064'>详细</a></div>
                                        </div>
                                    </div>
                                </div>
                            </li>


                            <li>
                                <div class="list-item"><span class="badge-arrow3">
在线拍
                                    </span><span class="badge-icon badge-bg103">即将开始
                                    </span>
                                    <a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16065"><img src="http://imgcdn.gpai.net/upload/courtfile/2018-1/201801031324558858.jpg" alt="" /></a>
                                    <div class="item-tit"><a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16065">合肥市马鞍山南路新都会联邦花园8幢105室</a></div>
                                    <div class="gpai-infos">
                                        <p><p><span>起拍价：</span><b class='price-red'>1058400</b><span class='price-red'>元</span></p> </p>

                                            <p><span>评估价：</span> <span><b>189</b>万元</span></p>
                                        <p><span>开始时间：2018-04-16 10:00:00</span> </p>
                                        <div class="m-infos-people clearfix">
                                            <span class="dif-line"></span>
                                            <div class="whalf fl">0 <span>次出价</span></div>
                                            <div class="whalf fr"><a href='http://www.gpai.net/sf\item2.do?Web_Item_ID=16065'>详细</a></div>
                                        </div>
                                    </div>
                                </div>
                            </li>


                            <li>
                                <div class="list-item"><span class="badge-arrow3">
在线拍
                                    </span><span class="badge-icon badge-bg103">即将开始
                                    </span>
                                    <a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16134"><img src="http://imgcdn.gpai.net/upload/courtfile/2018-3/201803151132533340.jpg" alt="" /></a>
                                    <div class="item-tit"><a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16134">上海市宝山区蕴川路1498弄152号801室</a></div>
                                    <div class="gpai-infos">
                                        <p><p><span>起拍价：</span><b class='price-red'>4220000</b><span class='price-red'>元</span></p> </p>

                                            <p><span>评估价：</span> <span><b>602.05</b>万元</span></p>
                                        <p><span>开始时间：2018-05-08 10:00:00</span> </p>
                                        <div class="m-infos-people clearfix">
                                            <span class="dif-line"></span>
                                            <div class="whalf fl">0 <span>次出价</span></div>
                                            <div class="whalf fr"><a href='http://www.gpai.net/sf\item2.do?Web_Item_ID=16134'>详细</a></div>
                                        </div>
                                    </div>
                                </div>
                            </li>


                            <li>
                                <div class="list-item"><span class="badge-arrow3">
在线拍
                                    </span><span class="badge-icon badge-bg103">即将开始
                                    </span>
                                    <a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16243"><img src="http://imgcdn.gpai.net/upload/courtfile/2018-3/201803201350125365.jpg" alt="" /></a>
                                    <div class="item-tit"><a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16243">上海市浦东新区浦东南路1969号306室</a></div>
                                    <div class="gpai-infos">
                                        <p><p><span>起拍价：</span><b class='price-red'>2891000</b><span class='price-red'>元</span></p> </p>

                                            <p><span>评估价：</span> <span><b>413</b>万元</span></p>
                                        <p><span>开始时间：2018-05-08 10:00:00</span> </p>
                                        <div class="m-infos-people clearfix">
                                            <span class="dif-line"></span>
                                            <div class="whalf fl">0 <span>次出价</span></div>
                                            <div class="whalf fr"><a href='http://www.gpai.net/sf\item2.do?Web_Item_ID=16243'>详细</a></div>
                                        </div>
                                    </div>
                                </div>
                            </li>


                            <li>
                                <div class="list-item"><span class="badge-arrow3">
在线拍
                                    </span><span class="badge-icon badge-bg103">即将开始
                                    </span>
                                    <a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16244"><img src="http://imgcdn.gpai.net/upload/courtfile/2018-3/201803201400292184.jpg" alt="" /></a>
                                    <div class="item-tit"><a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16244">上海市浦东南路1967、1969号地下一层车位47、48、55-65、72-86</a></div>
                                    <div class="gpai-infos">
                                        <p><p><span>起拍价：</span><b class='price-red'>5488000</b><span class='price-red'>元</span></p> </p>

                                            <p><span>评估价：</span> <span><b>784</b>万元</span></p>
                                        <p><span>开始时间：2018-05-08 10:00:00</span> </p>
                                        <div class="m-infos-people clearfix">
                                            <span class="dif-line"></span>
                                            <div class="whalf fl">0 <span>次出价</span></div>
                                            <div class="whalf fr"><a href='http://www.gpai.net/sf\item2.do?Web_Item_ID=16244'>详细</a></div>
                                        </div>
                                    </div>
                                </div>
                            </li>


                            <li>
                                <div class="list-item"><span class="badge-arrow3">
在线拍
                                    </span><span class="badge-icon badge-bg103">即将开始
                                    </span>
                                    <a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16246"><img src="http://imgcdn.gpai.net/upload/courtfile/2018-3/201803201432436732.jpg" alt="" /></a>
                                    <div class="item-tit"><a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16246">上海市浦东新区浦东南路1969号1417室</a></div>
                                    <div class="gpai-infos">
                                        <p><p><span>起拍价：</span><b class='price-red'>1869000</b><span class='price-red'>元</span></p> </p>

                                            <p><span>评估价：</span> <span><b>267</b>万元</span></p>
                                        <p><span>开始时间：2018-05-08 10:00:00</span> </p>
                                        <div class="m-infos-people clearfix">
                                            <span class="dif-line"></span>
                                            <div class="whalf fl">0 <span>次出价</span></div>
                                            <div class="whalf fr"><a href='http://www.gpai.net/sf\item2.do?Web_Item_ID=16246'>详细</a></div>
                                        </div>
                                    </div>
                                </div>
                            </li>


                            <li>
                                <div class="list-item"><span class="badge-arrow3">
在线拍
                                    </span><span class="badge-icon badge-bg103">即将开始
                                    </span>
                                    <a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16302"><img src="http://imgcdn.gpai.net/upload/courtfile/2018-3/201803222235249755.jpg" alt="" /></a>
                                    <div class="item-tit"><a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16302">上海市浦明路1288弄1号1202室</a></div>
                                    <div class="gpai-infos">
                                        <p><p><span>起拍价：</span><b class='price-red'>12796000</b><span class='price-red'>元</span></p> </p>

                                            <p><span>评估价：</span> <span><b>1828</b>万元</span></p>
                                        <p><span>开始时间：2018-05-08 10:00:00</span> </p>
                                        <div class="m-infos-people clearfix">
                                            <span class="dif-line"></span>
                                            <div class="whalf fl">0 <span>次出价</span></div>
                                            <div class="whalf fr"><a href='http://www.gpai.net/sf\item2.do?Web_Item_ID=16302'>详细</a></div>
                                        </div>
                                    </div>
                                </div>
                            </li>


                            <li>
                                <div class="list-item"><span class="badge-arrow3">
在线拍
                                    </span><span class="badge-icon badge-bg103">即将开始
                                    </span>
                                    <a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16303"><img src="http://imgcdn.gpai.net/upload/courtfile/2018-3/201803221942402256.jpg" alt="" /></a>
                                    <div class="item-tit"><a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16303">上海市浦东新区浦明路1288弄1号1602室</a></div>
                                    <div class="gpai-infos">
                                        <p><p><span>起拍价：</span><b class='price-red'>13062000</b><span class='price-red'>元</span></p> </p>

                                            <p><span>评估价：</span> <span><b>1866</b>万元</span></p>
                                        <p><span>开始时间：2018-05-08 10:00:00</span> </p>
                                        <div class="m-infos-people clearfix">
                                            <span class="dif-line"></span>
                                            <div class="whalf fl">0 <span>次出价</span></div>
                                            <div class="whalf fr"><a href='http://www.gpai.net/sf\item2.do?Web_Item_ID=16303'>详细</a></div>
                                        </div>
                                    </div>
                                </div>
                            </li>


                            <li>
                                <div class="list-item"><span class="badge-arrow3">
在线拍
                                    </span><span class="badge-icon badge-bg103">即将开始
                                    </span>
                                    <a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16419"><img src="http://imgcdn.gpai.net/upload/courtfile/2018-3/201803301144194792.jpeg" alt="" /></a>
                                    <div class="item-tit"><a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16419">上海市万源路788弄20号701室房地产及地下1层车位423室</a></div>
                                    <div class="gpai-infos">
                                        <p><p><span>起拍价：</span><b class='price-red'>6923000</b><span class='price-red'>元</span></p> </p>

                                            <p><span>评估价：</span> <span><b>989</b>万元</span></p>
                                        <p><span>开始时间：2018-05-18 10:00:00</span> </p>
                                        <div class="m-infos-people clearfix">
                                            <span class="dif-line"></span>
                                            <div class="whalf fl">0 <span>次出价</span></div>
                                            <div class="whalf fr"><a href='http://www.gpai.net/sf\item2.do?Web_Item_ID=16419'>详细</a></div>
                                        </div>
                                    </div>
                                </div>
                            </li>


                            <li>
                                <div class="list-item"><span class="badge-arrow3">
在线拍
                                    </span><span class="badge-icon badge-bg103">即将开始
                                    </span>
                                    <a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16469"><img src="http://imgcdn.gpai.net/upload/courtfile/2018-4/201804021115446225.jpg" alt="" /></a>
                                    <div class="item-tit"><a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16469">上海市普陀区常德路1258弄29、31号1001室—1008室房地产（整体拍卖）</a></div>
                                    <div class="gpai-infos">
                                        <p><p><span>起拍价：</span><b class='price-red'>12930000</b><span class='price-red'>元</span></p> </p>

                                            <p><span>评估价：</span> <span><b>1846.23</b>万元</span></p>
                                        <p><span>开始时间：2018-05-18 10:00:00</span> </p>
                                        <div class="m-infos-people clearfix">
                                            <span class="dif-line"></span>
                                            <div class="whalf fl">0 <span>次出价</span></div>
                                            <div class="whalf fr"><a href='http://www.gpai.net/sf\item2.do?Web_Item_ID=16469'>详细</a></div>
                                        </div>
                                    </div>
                                </div>
                            </li>


                            <li>
                                <div class="list-item"><span class="badge-arrow3">
在线拍
                                    </span><span class="badge-icon badge-bg103">即将开始
                                    </span>
                                    <a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16476"><img src="http://imgcdn.gpai.net/upload/courtfile/2018-2/201802061537216028.jpg" alt="" /></a>
                                    <div class="item-tit"><a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16476">上海市中山南路969号1902、1903、1904室办公房及地下2层19号车位</a></div>
                                    <div class="gpai-infos">
                                        <p><p><span>起拍价：</span><b class='price-red'>12370000</b><span class='price-red'>元</span></p> </p>

                                            <p><span>评估价：</span> <span><b>2207.61</b>万元</span></p>
                                        <p><span>开始时间：2018-05-18 10:00:00</span> </p>
                                        <div class="m-infos-people clearfix">
                                            <span class="dif-line"></span>
                                            <div class="whalf fl">0 <span>次出价</span></div>
                                            <div class="whalf fr"><a href='http://www.gpai.net/sf\item2.do?Web_Item_ID=16476'>详细</a></div>
                                        </div>
                                    </div>
                                </div>
                            </li>


                            <li>
                                <div class="list-item"><span class="badge-arrow3">
在线拍
                                    </span><span class="badge-icon badge-bg103">即将开始
                                    </span>
                                    <a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16480"><img src="http://imgcdn.gpai.net/upload/courtfile/2018-2/201802071017297622.jpg" alt="" /></a>
                                    <div class="item-tit"><a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16480">上海市浦东新区惠南镇盐大路2555号1-3层，2557号1-3层商业房地产</a></div>
                                    <div class="gpai-infos">
                                        <p><p><span>起拍价：</span><b class='price-red'>2440000</b><span class='price-red'>元</span></p> </p>

                                            <p><span>评估价：</span> <span><b>433.1</b>万元</span></p>
                                        <p><span>开始时间：2018-05-18 10:00:00</span> </p>
                                        <div class="m-infos-people clearfix">
                                            <span class="dif-line"></span>
                                            <div class="whalf fl">0 <span>次出价</span></div>
                                            <div class="whalf fr"><a href='http://www.gpai.net/sf\item2.do?Web_Item_ID=16480'>详细</a></div>
                                        </div>
                                    </div>
                                </div>
                            </li>


                            <li>
                                <div class="list-item"><span class="badge-arrow3">
在线拍
                                    </span><span class="badge-icon badge-bg103">即将开始
                                    </span>
                                    <a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16481"><img src="http://imgcdn.gpai.net/upload/courtfile/2018-4/201804031114149546.jpg" alt="" /></a>
                                    <div class="item-tit"><a href="http://www.gpai.net/sf\item2.do?Web_Item_ID=16481">上海市闵行区万源路986弄36号1001室（公寓）及23号地下1层车位783室</a></div>
                                    <div class="gpai-infos">
                                        <p><p><span>起拍价：</span><b class='price-red'>9002000</b><span class='price-red'>元</span></p> </p>

                                            <p><span>评估价：</span> <span><b>1286</b>万元</span></p>
                                        <p><span>开始时间：2018-05-18 10:00:00</span> </p>
                                        <div class="m-infos-people clearfix">
                                            <span class="dif-line"></span>
                                            <div class="whalf fl">0 <span>次出价</span></div>
                                            <div class="whalf fr"><a href='http://www.gpai.net/sf\item2.do?Web_Item_ID=16481'>详细</a></div>
                                        </div>
                                    </div>
                                </div>
                            </li>


                        </ul>
                    </div>
                    

                </div>
            </div>
            <!-- 内容部分end  -->
<input type="hidden" id="cityNum" name="cityNum" value="">
<input type="hidden" id="sQuy" name="sQuy" value="http://www.gpai.net/sf/court.do?id=1101&at=376&restate=1&">


<!-- footer -->
<div class="footer">
<div class="auto">
 <div class="footer-logo">
 <img src="/images/logo.png" alt="" />
 </div>
 <div class="footer-ul">
 <li class='w125'>
 关于公拍网 <br/>
 <a href="help.do?Action=about1">•公拍网 </a>
 <a href="help.do?Action=about2">•上海公拍中心 </a>
 <a href="help.do?Action=about3">•公拍大事记 </a>
 <a href="help.do?Action=about4">•诚聘英才 </a>
 <a href="help.do?Action=about5">•联系我们</a>
 </li>
 
 <li class='w125'>竞买帮助 <br/>
 <a href="help.do?Action=help6">•什么是同步拍卖</a>
 <a href="help.do?Action=help5">•什么是在线拍卖 </a>
 <a href="help.do?Action=jon">•如何参加司法拍卖 </a>
 <a href="help.do?Action=price">•什么是保留价 </a>
 <a href="help.do?Action=bid9">•如何设置代理出价</a>
 </li>
     
 <li class='w350'>
 拍卖课堂 <br/>
 <a href="help.do?Action=law1">•中华人民共和国拍卖法  </a>
 <a href="help.do?Action=law2">•人民法院民事执行中拍卖、变卖财产的规定 </a>
 <a href="help.do?Action=law3">•拍卖监督管理办法 </a>
 <a href="help.do?Action=law4">•中华人民共和国企业国有资产法</a>
 <a href="help.do?Action=law5">•拍卖师执业资格制度暂行规定</a>
 </li>
 </div>
</div>
</div>
<!-- bottom -->
<div class="bottom">
Copyright &copy; 2010-2016 上海市拍卖行业协会 版权所有 <a href="http://www.miibeian.gov.cn">沪ICP备11015601-3</a> <br/>地址：上海市黄浦区乔家路2号 邮编：200010 电话：400-820-3720
 传真：021-64226596 邮箱：webmaster@gpai.net
<div style="width:300px;margin:0 auto; ">
                 <a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31010102002574" style="display:inline-block;text-decoration:none;height:20px;line-height:20px;">
                <img src="/images/ga.png" style="float:left;" title="10.0.0.1"/><p style="float:left;height:20px;line-height:20px;margin: 0px 0px 0px 5px; color:#939393;">沪公网安备 31010102002574号</p></a>
             </div>

</div>
</div>



<script type="text/javascript" src="/plugin/jquery/jquery.min-1.11.0.js"></script>
<script src="/plugin/superslide/superslide.2.1.js"></script>
<script src="/common/common.js"></script>
<script src="js/webjs.js"></script>




    <script type="text/javascript">
        $(function(){
            $('.s-tab-item .condition li').each(function(){
                var _ltr = $(this).closest('.s-tab-item').position().left;
                $(this).click(function(){
                    var _lt = $(this).position().left;
                    var _dift = _ltr-_lt;
                    $(this).closest('.s-tab-item').find('.unlimited a').removeClass('selected');
                    $(this).find('.s-subtab').css('left',_dift+'px');
                    $(this).addClass('hover').siblings().removeClass('hover');
                });
                $(this).find('DELa').click(function(e){
                    e.preventDefault();
                    //alert(11);
                    $(this).closest('.condition').find('.selected').removeClass('selected');
                    $(this).addClass('selected'); 
                });
            });

            $('.DELs-tab-item .unlimited a').click(function(e){
                e.preventDefault();
                $(this).closest('.s-tab-item').find('.condition li').removeClass('hover');
                $(this).closest('.s-tab-item').find('.condition .selected').removeClass('selected');
                $(this).addClass('selected');
            });



            $('.filt-item-arrow .filt-item-tit').click(function(){
                $(this).closest('.filt-item-arrow').toggleClass('hover');
            });

            //$("#liCity").click();
            //fn_loadCity();
        });
            
        $(function() {   
               $(".filt-slidedown select").each(function() {
                var $this = $(this), h = 330, oplg = $this.find("option").length;
                var ulh = oplg > 15 ? h : oplg * 22,
                    ttop = $this.offset().top + ulh;
                if (oplg == 0) return;
                $this.hide(); //隐藏本身
                var width = $this.width();
                if (width == 0) width = 100;
                var DIV = $("<div>", { 'class': $this.attr("newclass") || 'label_selected' }).css('width', width),
                    INPUT = $("<span/>").css('width', width - 25),
                    UL = $("<ul>"), tOut;
                if (ttop > $(document).height()) {
                    UL.css('top', -0 - (ulh + 2));
                }
                UL.width(width);
                //创建选项
                $this.find("option").each(function () {
                    var $$this = $(this);
                    $("<li>", { 'id': $$this.val() || $$this.html(), 'html': ($this.attr("specialIcon") || "") + $$this.html() }).click(function () {
                        var val = $(this).attr("id"),
                            txt = $$this.html();
                        INPUT.html(txt);
                        UL.hide();
                        if ($this.find("option:selected").html() == txt) return false;
                        $this.find("option").removeAttr("selected");
                        if (val) {
                            $this.find("option[value='" + val + "']").attr("selected", true);
                        } else {
                            $this.find(":contains('" + txt + "')").attr("selected", true);
                        }
                        $this.triggerHandler("change");
                        return false;
                    }).appendTo(UL)
                });
                UL.find('li').prepend("<i class='right-icon'></i>");
                if (oplg > 15) UL.css("height", h);
                INPUT.html($this.find("option:selected").html() || $this.find("option:eq(0)").html());
                INPUT.appendTo(DIV);
                UL.appendTo(DIV);
                INPUT.focus(function () { UL.hide(); return false; });
                DIV.click(function () {
                    clearTimeout(tOut);
                    UL.css({ 'z-index': parseInt(UL.css("z-index")) + 1 }).show();
                    return false;
                }).hover(function () {
                    clearTimeout(tOut);
                }, function () {
                    tOut = setTimeout(function () { UL.hide(); }, 500);
                    return false;
                });
                $this.after(DIV);
            });
            
        });

        </script>
</body>
</html>
'''
my_dict = {}
labelList = re.findall(re.compile(r'<label>(.*?)</label>'), html.decode('utf8'))
pageList = re.findall(re.compile(r'class="page-infos"><label>(.*?)</label>'), html.decode('utf8'))
if labelList[0]>0:
    urlList = re.findall(re.compile(r'<a href="(.*?)item2.do?(.*?)"><img'), html.decode('utf8'))
    for urls in urlList:
        print 'http://www.gpai.net/sf/item2.do'+urls[1]
    
pageList = re.findall(re.compile(r'class="page-infos"><label>(.*?)</label>'), html.decode('utf8'))
if pageList.__len__() !=0:
    pageNum = pageList[0][1:2]
    print pageNum
else:
    pageNum = 1
    print pageNum





