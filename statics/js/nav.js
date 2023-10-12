var oBtn = document.getElementById("close")


/* 夜间模式 - 日间模式*/
//开关
var mode_switch = document.getElementById("mode-switch")
//属性
var nav = document.getElementById("mode")
var all = document.getElementById("all-mode")
var serve = document.getElementById("serve")
var line = document.getElementById("line")
var line1 = document.getElementById("line1")

//关闭页面，删除页面历史记录
oBtn.onclick = function() {
    window.history.replaceState(null, "", "/login/")
    window.history.go(0);
}


mode_switch.onclick = function (){
    if (nav.style.background === "rgb(70, 69, 71)"){
        //日间
        nav.style.setProperty('background', '#b0c4de', 'important');
        all.style.setProperty('background', '#f0fcff', 'important');
        all.style.setProperty('color','#464547', 'important')
        line.style.setProperty('background','#464547')
        line1.style.setProperty('background','#464547')
        serve.style.setProperty('background','#f0fcff', 'important')
    }else {
        //夜间
        nav.style.setProperty('background', '#464547', 'important')
        all.style.setProperty('background', '#999999', 'important');
        all.style.setProperty('color','#FFFFFF99', 'important')
        line.style.setProperty('background','#FFFFFF99')
        line1.style.setProperty('background','#FFFFFF99')
        serve.style.setProperty('background','#000000B2', 'important')
    }
}