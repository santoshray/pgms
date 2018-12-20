let navItemProfile = document.querySelector('.nav__item__profile');
let navItemIdVerification = document.querySelector('.nav__item__idVerification');
let navItemCompanyInfo = document.querySelector('.nav__item__companyInfo');
let navItemEmergencyContact = document.querySelector('.nav__item__emergencyContact');

navItemProfile.addEventListener('click', showProfile);
navItemIdVerification.addEventListener('click', showIdVerification);
navItemProfile.addEventListener('click', showCompanyInfo);
navItemProfile.addEventListener('click', showEmergencyContact);
let pgManagementProfile = document.querySelector('.pg-management-profile');
let pgManagementProfileStatus = pgManagementProfile.style.display;
let pgManagementIdVerification = document.querySelector('.pg-management-idVerification');
let pgManagementIdVerificationStatus = pgManagementIdVerification.style.display;
let pgManagementCompanyInfo = document.querySelector('.pg-management-companyInfo');
let pgManagementCompanyInfoStatus = pgManagementCompanyInfo.style.display;
let pgManagementEmergencyContact = document.querySelector('.pg-management-emergencyContact');
let pgManagementEmergencyContactStatus = pgManagementEmergencyContact.style.display;
let displayLink = "";

function hideall(){
  pgManagementProfile.style.display = "none";
  pgManagementIdVerification.style.display = "none";
  pgManagementCompanyInfo.style.display = "none";
  pgManagementEmergencyContact.style.display = "none";

}
function checkDisplayEachLink(){
  if(pgManagementProfile.style.display == "block"){
//    displayLink = pgManagementProfile.style.display;
//    pgManagementProfile.style.display = "none";
  }
  if(pgManagementIdVerification.style.display == "block"){
  //  displayLink = pgManagementIdVerificationStatus;
    pgManagementIdVerification.style.display = "none";
  }
  if(pgManagementIdVerification.style.display == "block"){
    // displayLink = pgManagementCompanyInfoStatus;
    pgManagementIdVerification.style.display = "none";
  }
  if(pgManagementEmergencyContact.style.display == "block"){
    // displayLink = pgManagementEmergencyContactStatus;
    pgManagementEmergencyContact.style.display = "none";
  }
}
function showProfile(){
  hideall();
  pgManagementProfile.style.display="block";
}
function showIdVerification(){
// checkDisplayEachLink();
  hideall();
  pgManagementIdVerification.style.display="block";
}
function showCompanyInfo(){
//  checkDisplayEachLink();
  hideall();
  pgManagementCompanyInfo.style.display="block";
}
function showEmergencyContact(){
//  checkDisplayEachLink();
  hideall();
  pgManagementEmergencyContact.style.display="block";
}
