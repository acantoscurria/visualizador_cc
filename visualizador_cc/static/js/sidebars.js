/* global bootstrap: false */
(function () {
  'use strict'
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl)
  })
})();



const btn_menu = document.querySelector(".btn-menu");
if (btn_menu) {
  btn_menu.addEventListener("click", () => {
    const menu_items = document.querySelector(".menu-dashboard-mobile");
    menu_items.classList.toggle("show");
    
  });
};

window.addEventListener('DOMContentLoaded', () => {
  const list = document.querySelectorAll(".lista i");
  function activeLink(){
    list.forEach((item)=>
    item.classList.remove('active'));
    this.classList.add('active');
  }
  list.forEach((item)=>
  item.addEventListener('click',activeLink));
});