// retrieve a visit count



window.addEventListener('DOMContentLoaded', (event) =>{
    //testfunc();
    getVisitCount();
})
//TODO: insert the link
const functionApiUrl = '';
//const localFunctionApi = 'http://localhost:7071/api/GetResumeCounter';


//const functionApiUrl = 'http://localhost:7071/api/GetResumeCounter';

const testfunc = () =>{
    document.getElementById("counter").innerText = "1000";
}

const getVisitCount = () => {
 /*   
    let response = fetch(functionApiUrl);
    var obj = JSON.parse(response)
    document.getElementById("counter").innerText = "100";
*/
    let count = 30;
    fetch(functionApiUrl).then(response => {return response.json()}).then(response =>{
        console.log("Website called function API.");
        count = response.count;
        document.getElementById("counter").innerText = count;
        //return count;
    })
    .catch(function(error){
        console.log(error);
    });
    return count;   

}