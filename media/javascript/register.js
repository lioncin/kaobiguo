//xlin 20121202
var Register = {};
Register.submitForm=function(){
	$('#register-content').validate({
		rules:{
			username:{required:true,maxlength:15},
			useremail:{required:true,email:true},
			userpassword:{required:true},
			userpassword2:{required:true,equalTo:'#userpassword'}
		},
		messages:{
			username:{
				required:'您还没有输入用户名',
				maxlength:'您输入的用户名长度大于15个字符'
			},
			useremail:{
				required:'您还没有输入电子邮箱',
				email:'电子邮箱格式不正确'
			},
			userpassword:{
				required:'您还没有输入密码'
			},
			userpassword2:{
				required:'您还没有输入密码',
				equalTo:'密码不一致，请再次确认'
			}
		},
		submitHandler:function(form){
			var email = $.trim($('#register-content input[name="username"]').val());
			var name = $.trim($('#register-content input[name="useremail"]').val());;
			//判断用户名和邮箱是否被注册过
			//var msg = Register.checkNameAndEmailExitst(name,email);
			//if(msg=='ok'){
			form.submit();
			//}
			
		}
	});
};

//判断用户名和邮箱是否被注册过
Register.checkNameAndEmailExitst=function(name,email){
	var url = '/register/ajax/checkNameAndEmailExitst/';
	$.ajax({
		url:url,
		type:'POST',
		data:{
			name:name,
			email:email
		},
		success:function(data,txtStatus){
			var d = JSON.parse(data);
			if(d=='ok'){
				return true;
			}else{
				return d['msg'];
			}
		},
		error:function(data,txtStatus){
			
		}
	});
};

$(function(){
	$('#submitRegister').cilck(function(){
		console.log(1111);
	});
});