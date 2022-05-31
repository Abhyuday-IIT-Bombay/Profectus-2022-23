$('select[name*="location"]').change(function() {
    var selectedOptions = $('select option:selected');
    $('select option').removeAttr('disabled');
    selectedOptions.each(function() {        
        var value = this.value;
        if (value !== ''){           
        var id = $(this).parent('select[name*="location"]').attr('id');
        var options = $('select:not(#' + id + ') option[value=' + value + ']');
        options.attr('disabled', 'true');
        }
    });
});	