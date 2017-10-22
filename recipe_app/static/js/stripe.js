$(function() {
  $("#register-form").submit(function() {
<<<<<<< HEAD
      var form = this;
=======
      var form = this;   
>>>>>>> 7b4c5c4a9f908f202fcb43d8f67b9fd44ebb7750
      var card = {
        number:   $("#id_credit_card_number").val(),
        expMonth: $("#id_expiry_month").val(),
        expYear:  $("#id_expiry_year").val(),
        cvc:      $("#id_cvv").val()
      };
<<<<<<< HEAD

=======
 
>>>>>>> 7b4c5c4a9f908f202fcb43d8f67b9fd44ebb7750
      $("#validate_card_btn").attr("disabled", true);
       Stripe.createToken(card, function(status, response) {
        if (status === 200) {
          console.log(status, response);
          $("#credit-card-errors").hide();
          $("#id_stripe_id").val(response.id);
          form.submit();
<<<<<<< HEAD

=======
 
>>>>>>> 7b4c5c4a9f908f202fcb43d8f67b9fd44ebb7750
        } else {
          $("#stripe-error-message").text(response.error.message);
          $("#credit-card-errors").show();
          $("#validate_card_btn").attr("disabled", false);
        }
      });
<<<<<<< HEAD
      return false;
  });
});
=======
      return false;    
  });
});
>>>>>>> 7b4c5c4a9f908f202fcb43d8f67b9fd44ebb7750
