//js for home page
$(function(){
	//调用函数，加载当前正在发布的消息
	getCurrentHotMsgs();
});

function getCurrentHotMsgs(){
	var url = 'ajax/getCurrentHotMsgs/';
	$.ajax({
		url:url,
		type:'POST',
		success:function(data,txtStatus){
			var d = JSON.parse(data);
			showCurrentHotMsgs(d);
		}
	});
}

function showCurrentHotMsgs(d){
	var html = '';
	if(d){
		html += '<p>目前没有数据</p>';
	}else{
		html += '<p>有很多数据</p>';
	}
	$('#publish-content').html(html);
}
