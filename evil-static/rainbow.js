"use strict";

(function () {
  var COLORS = [
    "#E81416",
    "#FFA500",
    "#FAEB36",
    "#79C314",
    "#487DE7",
    "#4B369D",
    "#70369D",
  ];

  var currentColorIndex = 0;

  setInterval(function () {
    document.querySelector("h2").style.color = COLORS[currentColorIndex];
    currentColorIndex = (currentColorIndex + 1) % COLORS.length;
  }, 500);
})();
