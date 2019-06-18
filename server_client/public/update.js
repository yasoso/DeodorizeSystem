$(function() {
    var POLLLING_INVERVAL_TIME_IN_MILLIS = 5000;//5.0s
    (function polling() {
        getSmellUpdate();
        window.setTimeout(polling, POLLLING_INVERVAL_TIME_IN_MILLIS);
        //console.log(req.body[0].smell);
      }());

    function getSmellUpdate() {
      $.ajax({
      type : "GET",
      url : "smellUpdate",
      content : "application/json",
      dataType : "json",
    }).done(function(data) {
      console.log(data.smell);
      var txt = "臭い：" + data.smell;
      document.getElementById("smellTxt").innerHTML = txt;
      //$("dd").text(data.count);//html要素変更する
    }).fail(function(jqXHR, textStatus) {
      $("dd").text("error occured");//html要素変更する
      });
    }

    function getCountUpdate() {
      $.ajax({
      type : "GET",
      url : "countUpdate",
      content : "application/json",
      dataType : "json",
    }).done(function(data) {
      console.log(data.smell);
      var txt = "消臭回数：" + data.count;
      document.getElementById("countTxt").innerHTML = txt;
      //$("dd").text(data.count);//html要素変更する
    }).fail(function(jqXHR, textStatus) {
      $("dd").text("error occured");//html要素変更する
      });
    }
  });
