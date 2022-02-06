var request = require('request'); 
var fs = require('fs');
// var friends = [{"name": "Ravi","phone":7061133910},
// // {"name": "Indiramam","phone":919926070125},
// {"name": "Rishi","phone":8109204148}
// ]
var urldata = `https://api.chat-api.com/instance391276/sendMessage?token=3gr24phq2pdoiu79`;
var urlfile = `https://api.chat-api.com/instance391276/sendFile?token=3gr24phq2pdoiu79`;
var urlforw = `https://api.chat-api.com/instance391276/forwardMessage?token=3gr24phq2pdoiu79`;
const filedata = fs.readFileSync('./file.txt', 'utf8');
for(let i =0; i < 100; i=i+1) {
    var data1 = {
        "body": filedata,
        "filename": "money.jpg",
        "phone": `918949904720`,
    }
    var data2 ={
        "phone": `918949904720`,
        "messageId": "true_916388637544@c.us_25444280B89849AC025512E95E2577A7"
      }
    
        // Send a request
        request({
            url: urlfile,
            method: "POST",
            json: data1
        });
        request({
            url: urlforw,
            method: "POST",
            json: data2
        });
    console.log("Message sent");
    // console.log(personaldata.Contact);
}
// //read data from xlsx file
//     var workbook = XLSX.readFile('testdata2.xlsx');
//     var sheet_name_list = workbook.SheetNames;
//     var xlData = XLSX.utils.sheet_to_json(workbook.Sheets[sheet_name_list[0]]);
//     console.log(xlData);
