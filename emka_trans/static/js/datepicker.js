var $j = jQuery.noConflict();

function available(date) {
  dmy = ('0' + date.getDate()).slice(-2) + "-" + ('0' + (date.getMonth()+1)).slice(-2) + "-" + date.getFullYear();
  if ($j.inArray(dmy, unavailableDates) == -1) {
    return [true, "","Available"];
  } else {
    return [false,"","unAvailable"];
  }
}

  $j( function() {
    $j( "#datepicker" ).datepicker({
        minDate: 2,
        beforeShowDay: available
    });
  } );