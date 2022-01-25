import Vue from 'https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.esm.browser.js'
new Vue({
    el: "#app",
    data () {
      return{
        
        users:null,
        
        errored:false,
        sign:{
          fname:"",
          lname:"",
          email:"",
          username:"",
        },
        
        submitted:false,
        liked:false,
      }
    },
    
    methods: {
    signup: function(){
      //let token = document.head.querySelector('meta[name="csrf-token"]');
      console.log("hello");
      axios.post("http://127.0.0.1:8000/accounts/user/create",{first_name:this.sign.fname,last_name:this.sign.lname,email:this.sign.email,username:this.sign.username}).then(response => {
        console.log("user created");
        this.sign.id = response.data.id;
          console.log(response.data);
          window.location.href="sawo.html";
      }).catch(error=>{
        this.errored =true
        console.log(this.errored);
      })
    
    }
}
  });
