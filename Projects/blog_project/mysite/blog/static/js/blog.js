// $(function(){
//     var r = Math.floor(Math.random()*254)+1;
//     var g = Math.floor(Math.random()*254)+1;
//     var b = Math.floor(Math.random()*254)+1;
//     var directionr = 'up';
//     var directiong = 'down';
//     var directionb = 'up';
    
//     setInterval(function(){
      
//       if(r == 0){
//         directionr = 'up';
//       }else if(r == 255){
//         directionr = 'down'; 
//       }else{
//         directionr = directionr;
//       }
      
//       if(directionr == 'up'){
//         r++;
//       }else if(directionr == 'down'){
//         r--;
//       }
      
//       $('.outer-section').css('background', 'rgb('+r+', '+g+', '+b+')');
      
//       $('span').css({
//         color: 'rgba('+r+', '+g+', '+b+', 0.1)'
//       });
      
//     });
    
//     setInterval(function(){
      
//       if(g == 0){
//         directiong = 'up';
//       }else if(g == 255){
//         directiong = 'down'; 
//       }else{
//         directiong = directiong;
//       }
      
//       if(directiong == 'up'){
//         g++;
//       }else if(directiong == 'down'){
//         g--;
//       }
      
//       $('.outer-section').css('background', 'rgb('+r+', '+g+', '+b+')');
      
//       $('span').css({
//         color: 'rgba('+r+', '+g+', '+b+', 0.1)'
//       });
      
//     }, 10);
    
//     setInterval(function(){
      
//       if(b == 0){
//         directionb = 'up';
//       }else if(b == 255){
//         directionb = 'down'; 
//       }else{
//         directionb = directionb;
//       }
      
//       if(directionb == 'up'){
//         b++;
//       }else if(directionb == 'down'){
//         b--;
//       }
      
//       $('.outer-section').css('background', 'rgb('+r+', '+g+', '+b+')');
      
//       $('span').css({
//         color: 'rgba('+r+', '+g+', '+b+', 0.1)'
//       });
      
//     }, 20);
    
//   })