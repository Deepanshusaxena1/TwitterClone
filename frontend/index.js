
import Vue from 'https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.esm.browser.js'

//console.log("Hello")
//axios.get("http://127.0.0.1:8000/feed/fetch?user_id=1").then(response => console.log(response));

//axios.get('https://api.npms.io/v2/search?q=axios').then(response => console.log(response));
//Vue.component("Navigation",Navigation);

    new Vue({
    el: "#app",
    data () {
      return{
        tweets:null,
        users:null,
        
        errored:false,
        content:{
          tweet:"",
        },
        comments:{
content:"",
        },
        
        submitted:false,
        liked:false,
      }
    },
    created(){
        //console.log("Hello 2.0");
      this.tweets=null
      this.users=null
      axios.get("http://127.0.0.1:8000/feed/fetch?user_id=2").then(response =>{
        console.log(response.data)
       this.tweets=response.data['tweets']
      }).catch(error => {
        //console.log(error)
        this.errored =true

      })
      axios.get("http://127.0.0.1:8000/accounts/user/fetch?user_id=2").then(response =>{
        console.log(response.data)
       this.users=response.data['user_data']
      }).catch(error => {
        //console.log(error)
        this.errored =true

      })

    },
    methods: {
    submit: function(){
      //let token = document.head.querySelector('meta[name="csrf-token"]');
      //console.log(token);
      axios.post("http://127.0.0.1:8000/feed/tweet/create",{content:this.content.tweet,user:2}).then(response => {
        console.log("tweet posted")
        this.feed.id = response.data.id;
          console.log(response.data);
      }).catch(error=>{
        this.errored =true
        console.log(this.errored);
      })
    
    },
    like_tweet:function(tweet,user){
      //console.log(tweet);
      axios.post("http://127.0.0.1:8000/feed/tweet/like",{tweet:tweet,user:user}).then(response => {
        console.log("like")
        this.like.id = response.data.id;
          console.log(response.data);
          this.liked=true;
      }).catch(error=>{
        this.errored =true
        console.log(this.errored);
        this.liked=false;
      })
      
    },
    
    comment_post:function(user,tweet){
      
      axios.post("http://127.0.0.1:8000/feed/comment/create",{content:this.comments.content,user:user,tweet:tweet}).then(response => {
        console.log("like")
        this.comments.id = response.data.id;
          console.log(response.data);
          this.liked=true;
      }).catch(error=>{
        this.errored =true
        console.log(this.errored);
        this.liked=false;
      })
      
    }
  }
  });


  