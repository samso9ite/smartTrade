// ==================================================
// Project Name  :  Printem - HTML5 Template
// File          :  JS Base
// Version       :  1.0.0
// Last change   :  05 Octobar 2020
// Author        :  BDevs (https://themeforest.net/user/bdevs)
// Developer:    :  Rakibul Islam Dewan
// ==================================================


(function($) {
  "use strict";


  // back to top - start
  // --------------------------------------------------
  $(window).scroll(function() {
    if ($(this).scrollTop() > 200) {
      $('#backtotop:hidden').stop(true, true).fadeIn();
    } else {
      $('#backtotop').stop(true, true).fadeOut();
    }
  });
  $(function() {
    $("#scroll").on('click', function() {
      $("html,body").animate({
        scrollTop: $("#thetop").offset().top
      }, "slow");
      return false
    })
  });
  // back to top - end
  // --------------------------------------------------


  // preloader - start
  // --------------------------------------------------
  $(window).on('load', function() {
    $('.preloader').addClass('loaded');

    if ($('.preloader').hasClass('loaded')) {
      $('.spinner').delay(1000).queue(function () {
        $(this).remove();
      });
    }
  });
  // preloader - end
  // --------------------------------------------------


  // background image - start
  // --------------------------------------------------
  $('[data-background]').each(function() {
    $(this).css('background-image', 'url('+ $(this).attr('data-background') + ')');
  });
  // background image - end
  // --------------------------------------------------


  // sticky header - start
  // --------------------------------------------------
  $(window).on('scroll', function () {
    if ($(this).scrollTop() > 120) {
      $('.sticky_header').addClass("stuck")
    } else {
      $('.sticky_header').removeClass("stuck")
    }
  });
  // sticky header - end
  // --------------------------------------------------


  // mobile menu - start
  // --------------------------------------------------
  $(document).ready(function () {
    $('.close_btn, .overlay').on('click', function () {
      $('.mobile_menu').removeClass('active');
      $('.overlay').removeClass('active');
      $('.mobile_menu_list ul a').removeClass('active');
    });

    $('.mobile_menu_list ul a').on('click', function () {
      $('.mobile_menu').removeClass('active');
      $('.overlay').removeClass('active');
    });

    $('.menu_btn').on('click', function () {
      $('.mobile_menu').addClass('active');
      $('.overlay').addClass('active');
    });
  });
  // mobile menu - end
  // --------------------------------------------------


  // scroll animation - start
  // --------------------------------------------------
  var wow = new WOW({
    offset: 100,
    mobile: true,
    duration: 1000,
    boxClass: 'wow',
    animateClass: 'animated',
  });
  wow.init();
  // scroll animation - end
  // --------------------------------------------------


})(jQuery);