var express = require('express');
var path = require('path');
var app = express();
var PORT = 3000;
var request = require('request');
var data;
var options = {
  'method': 'POST',
  'url': 'https://api.razorpay.com/v1/orders',
  'headers': {
    'Authorization': 'Basic cnpwX3Rlc3RfalpPUGVnZk9xbVZtOWI6VEVNOExXc29TdmxkRHpOR25XY002TDMz',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "amount": 100,
    "currency": "INR",
    "receipt": "rcptid_11"
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
//   console.log(response.body);
  data = JSON.parse(response.body);
});


// Without middleware
app.get('/', function(req, res){
    var options ={
        "key": "YOUR_KEY_ID", // Enter the Key ID generated from the Dashboard
        "amount": "50000", // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
        "currency": "INR",
        "name": "Prestige Institue",
        "description": "Test Transaction",
        "image": "https://example.com/your_logo",
        "order_id": data["id"], //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
        "handler": function (response){
            alert(response.razorpay_payment_id);
            alert(response.razorpay_order_id);
            alert(response.razorpay_signature)
        },
        "prefill": {
            "name": "Gaurav Kumar",
            "email": "gaurav.kumar@example.com",
            "contact": "9999999999"
        },
        "notes": {
            "address": "Razorpay Corporate Office"
        },
        "theme": {
            "color": "#3399cc"
        }
    };
    var rzp1 = new Razorpay(options);
    rzp1.on('payment.failed', function (response){
            alert(response.error.code);
            alert(response.error.description);
            alert(response.error.source);
            alert(response.error.step);
            alert(response.error.reason);
            alert(response.error.metadata.order_id);
            alert(response.error.metadata.payment_id);
    });
    document.getElementById('rzp-button1').onclick = function(e){
        rzp1.open();
        e.preventDefault();
    }
	res.json({ data });
});

app.get('/pay', function(req, res){
    res.sendFile(path.join(__dirname+'/index.html'));
	
});
app.listen(PORT, function(err){
	if (err) console.log(err);
	console.log("Server listening on PORT", PORT);
});


// var options ={
//     "key": "YOUR_KEY_ID", // Enter the Key ID generated from the Dashboard
//     "amount": "50000", // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
//     "currency": "INR",
//     "name": "Prestige Institue",
//     "description": "Test Transaction",
//     "image": "https://example.com/your_logo",
//     "order_id": data["id"], //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
//     "handler": function (response){
//         alert(response.razorpay_payment_id);
//         alert(response.razorpay_order_id);
//         alert(response.razorpay_signature)
//     },
//     "prefill": {
//         "name": "Gaurav Kumar",
//         "email": "gaurav.kumar@example.com",
//         "contact": "9999999999"
//     },
//     "notes": {
//         "address": "Razorpay Corporate Office"
//     },
//     "theme": {
//         "color": "#3399cc"
//     }
// };
// var rzp1 = new Razorpay(options);
// rzp1.on('payment.failed', function (response){
//         alert(response.error.code);
//         alert(response.error.description);
//         alert(response.error.source);
//         alert(response.error.step);
//         alert(response.error.reason);
//         alert(response.error.metadata.order_id);
//         alert(response.error.metadata.payment_id);
// });
// document.getElementById('rzp-button1').onclick = function(e){
//     rzp1.open();
//     e.preventDefault();
// }