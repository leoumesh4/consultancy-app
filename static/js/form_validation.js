
    function validateForm() {
      var x = document.forms["contact_form"]["name"].value;
      var y = document.forms["contact_form"]["email"].value;
      var z = document.forms["contact_form"]["phone"].value;

      if (x == "") {
        alert("Name must be filled out");
        return false;
      }

      if (y == "") {
        alert("Email must be filled out.");
        return false;
      }

      if (z == "") {
        alert("Phone must be filled out");
        return false;
      }
}
