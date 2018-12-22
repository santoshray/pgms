let navItemProfile = document.querySelector('.nav__item__profile');
let navItemIdVerification = document.querySelector('.nav__item__idVerification');
let navItemCompanyInfo = document.querySelector('.nav__item__companyInfo');
let navItemEmergencyContact = document.querySelector('.nav__item__emergencyContact');

navItemProfile.addEventListener('click', showProfile);
navItemIdVerification.addEventListener('click', showIdVerification);
navItemCompanyInfo.addEventListener('click', showCompanyInfo);
navItemEmergencyContact.addEventListener('click', showEmergencyContact);
let pgManagementProfile = document.querySelector('.pg-management-profile');
let pgManagementIdVerification = document.querySelector('.pg-management-idVerification');
let pgManagementCompanyInfo = document.querySelector('.pg-management-companyInfo');
let pgManagementEmergencyContact = document.querySelector('.pg-management-emergencyContact');

hideall();
function hideall(){
  pgManagementProfile.style.display = "none";
  pgManagementIdVerification.style.display = "none";
  pgManagementCompanyInfo.style.display = "none";
  pgManagementEmergencyContact.style.display = "none";

}

function showProfile(){
  hideall();
  pgManagementProfile.style.display="block";
}
function showIdVerification(){
  hideall();
  pgManagementIdVerification.style.display="block";
}
function showCompanyInfo(){
  hideall();
  pgManagementCompanyInfo.style.display="block";
}
function showEmergencyContact(){
  hideall();
  pgManagementEmergencyContact.style.display="block";
}
