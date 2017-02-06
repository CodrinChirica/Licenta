$(document).ready(function () {
  //your code here
  /* activate scrollspy menu */
  $('body').scrollspy({
    target: '#navbar-collapsible',
    offset: 50
  });

  /* smooth scrolling sections */
  $('a[href*=#]:not([href=#])').click(function() {
      if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
        if (target.length) {
          $('html,body').animate({
            scrollTop: target.offset().top - 50
          }, 1000);
          return false;
        }
      }
  });

  //----------------------Mobile Screenshot-----------------------------
  var mobileScreenshot_deviceSelected = $( "#mobileScreenshot-select-device" );
  var mobileScreenshot_customScreenSizeBlock = $( "#mobileScreenshot-customScreenSize-optional" );
  mobileScreenshot_ShowOrHide_customScreenSizeBlock();

  function mobileScreenshot_ShowOrHide_customScreenSizeBlock(){
    if(mobileScreenshot_deviceSelected.prop('selectedIndex') != 6){
      mobileScreenshot_customScreenSizeBlock.hide();
    }
    else{
      mobileScreenshot_customScreenSizeBlock.show();
    }
  }

    
  mobileScreenshot_deviceSelected.change(function(){
    mobileScreenshot_ShowOrHide_customScreenSizeBlock();
  });


  //----------------------AJAX-----------------------------
  var csrftoken = Cookies.get('csrftoken');

  //----------------------Rank Checker-----------------------------
  rankForm = $("#rankChecker");
  rankForm.submit(function(event){
      AjaxCall(rankForm, rankSuccesFct)
      return false; //<---- move it here
  });

  function rankSuccesFct(json){
    console.log(json);
    $('#google_rank').text(json['google_rank'])
      // $.each(json, function() {
      //     $.each(this, function(option_id, price) {
      //         var element = $(".list-group-item[id='"+option_id+"']");
      //         element = element.children(".product-price");
      //         // console.log(element.attr('name'));
      //         element.attr('name', price) ;
      //         element.html(price) ;
      //     });
      // });
  }

  function AjaxCall(form, successFct=null, errorFct=null){
      $.ajax({
          type: form.attr('method'),
          url: form.attr('action'),
          data: form.serialize(),
          success : successFct,
          error : errorFct
      });
  }

});