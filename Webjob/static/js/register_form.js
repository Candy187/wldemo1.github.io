var phoneObj;
var emailObj;
var usernameObj;
var passwordObj;
var confirmObj;
var phoneMsg;
var emailMsg;
var usernameMsg;
var passwordMsg;
var confirmMsg;

window.onload = function(){
	phoneObj = document.getElementById("phonenumber");
	emailObj = document.getElementById("email");
	usernameObj = document.getElementById("username");
	passwordObj = document.getElementById("password");
	confirmObj = document.getElementById("repassword");
	phoneMsg = document.getElementById("phoneMsg");
	emailMsg = document.getElementById("emailMsg");
	usernameMsg = document.getElementById("usernameMsg");
	passwordMsg = document.getElementById("confirmMsg");
};

function Checkform(){
	var bphone = checkPhoneNumber();
	var busername = checkUsername();
	var bpassword = checkPassword();
	var bconfirm = checkConfirm();
	return bphone && busername && bpassword && bconfirm;
}

function checkPhoneNumber(){
	var reg = /^0?(13[0-9]|15[012356789]|18[012346789]|14[57]|17[678]|170[059]|14[57]|166|19[89])[0-9]{8}$/;
	var value = phoneObj.value;
	var msg = "";
	if(!value)
		msg = "手机号码必须填写。";
	else if(!reg.test(value))
		msg = "手机号码格式不合法。";
	phoneMsg.innerHTML = msg;
	phoneObj.parentNode.parentNode.style.color = msg == "" ? "#6A6969" : "red";
	return msg = "";	
}

function checkEmail(){
	var reg = /^[\w-]+@([\w-]+\.)+[a-zA-Z]{2,4}$/;
	var value = emailObj.value;
	var msg = "";
	if(!value)
		msg = "邮箱必须填写。";
	else if(!reg.test(value))
		msg = "该邮箱无效。";
	emailMsg.innerHTML = msg;
	emailObj.parentNode.parentNode.style.color = msg == "" ? "#6A6969" : "red";
	return msg = "";
}

function checkUsername(){
	var reg = /^[a-zA-Z]\w{0,9}$/;
	var value = usernameObj.value;
	var msg = "";
	if(!value)
		msg = "用户名必须填写。";
	else if(!reg.test(value))
		msg = "用户名不合法。";
	usernameMsg.innerHTML = msg;
	usernameObj.parentNode.parentNode.style.color = msg == "" ? "#6A6969" : "red";
	return msg = "";	
}

function checkPassword(){
	var reg = /^.{6,16}$/;
	var value = passwordObj.value;
	var msg = "";
	if(!value)
		msg = "密码必须填写。";
	else if(!reg.test(value))
		msg = "密码不合法。";
	passwordMsg.innerHTML = msg;
	passwordObj.parentNode.parentNode.style.color = msg == "" ? "#6A6969" : "red";
	return msg = "";	
}

function checkConfirm(){
	var passwordValue = passwordObj.value;
	var confirmValue = confirmObj.value;
	var msg = "";
	if(!confirmValue)
		msg = "确认密码必须填写。";
	else if(passwordValue != confirmValue)
		msg = "密码必须保持一致。";
	confirmMsg.innerHTML = msg;
	confirmObj.parentNode.parentNode.style.color = msg == "" ? "#6A6969" : "red";
	return msg = "";	
}

