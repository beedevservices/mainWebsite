function openTab01(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent01")
    for (i=0; i<tabcontent.length; i++) {
        tabcontent[i].style.display = 'none'
    }
    tablinks = document.getElementsByClassName('tablinks01')
    for (i=0; i<tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace("active", "")
    }
    document.getElementById(tabName).style.display = "block"
    evt.currentTarget.className += " active"
}
document.getElementById('defaultOpen01').click()

function openTab02(tabName, elemt, color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent02")
    for (i=0; i<tabcontent.length; i++) {
        tabcontent[i].style.display = "none"
    }
    tablinks = document.getElementsByClassName('tablinks02')
    for (i=0; i<tablinks.length; i++) {
        tablinks[i].style.backgroundColor = ""
    }
    document.getElementById(tabName).style.display = "block"
    elemt.style.backgroundColor = color
}
document.getElementById('defaultOpen02').click()

function openTab03(pageName,elmnt,color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent03");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks03");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
    }
    document.getElementById(pageName).style.display = "block";
    elmnt.style.backgroundColor = color;
}

document.getElementById("defaultOpen03").click();