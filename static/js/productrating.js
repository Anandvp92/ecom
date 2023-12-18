<script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.4.1.min.js"></script>


function updatestar(productid,datavalue){
    const stars = document.querySelectorAll('.star-'+productid);
      stars.forEach((star, index) => {
        if (index < datavalue) {
          star.classList.add('active');
      } else {
          star.classList.remove('active');
      }
      });
  }
  
  
  function testfun(productid,datavalue){
      const csrfInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
      let i = document.getElementById('rating-'+productid);   
      i.innerHTML=datavalue;
      Backend(productid,datavalue,csrfInput.value);
      updatestar(productid,datavalue);
      
  }
  
  
  function starr(productid,datavalue){
      let i = document.getElementById('rating-'+productid);   
      i.innerHTML=datavalue;
      Backend(productid,datavalue,csrfInput.value);
      updatestar(productid,datavalue);
      
  }
  
  
  function Backend(productid,datavalue,csrfToken){
      $.ajax({
          type: "POST",
          url: "{% url 'test' %}",
          headers: {
              "X-CSRFToken": csrfToken,
          },
          data: { 'value': productid,
                  'rating': datavalue,                  
        },
      });
  
  
  }