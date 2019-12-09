import React from 'react';
import TextField from '@material-ui/core/TextField';
import EventIcon from '@material-ui/icons/Event';
import Button from '@material-ui/core/Button';
import { withStyles } from '@material-ui/styles';

import axios from 'axios';

const styles = theme => ({
    divbyAndy: {
        padding: '10px 20px 40px 20px'
    },

    paper: {
        padding: 10,
        margin: 10,
        maxWidth: 700
    },
    textField: {
        paddingRight: 5,
    },
    textFields: {
        paddingTop: 10,
        paddingBottom: 10,
    },
    button: {
        backgroundColor: "#4998e6"
    }
  });

class CreateEvent extends React.Component {
    constructor(props){
        super(props);
        this.state={
            uid: this.props.uid,
            username : this.props.username,
            gid: this.props.gid,
            gpp: this.props.gpp, // public private
            event_name: "",
            event_location: "",
            event_date_time: JSON.stringify(new Date()).slice(1, 17),
        }
    }

    createEvent = (e) =>{
        e.preventDefault();

        // url login
        var apiBaseUrl = "http://35.202.227.79:5000/";
        var self = this;

        // format date for  backend
        let date = this.state.event_date_time.split("T")[0];
        let time = this.state.event_date_time.split("T")[1];
        
        /* POPULATE */
        let userinfo = {
            uid: this.state.uid,
            gid: this.state.gid,
            host: this.state.username,
            event_name: this.state.event_name,
            location: this.state.event_location,
            e_date: date,
            e_time: time,
            public_or_private: this.state.gpp
        };

        var config = {
            headers: {
                'Access-Control-Allow-Origin': '*'
            },
            withCredentials: false
        };
        // post it to the backends
        axios.post(apiBaseUrl + 'add-event', userinfo, config).then(function (response) {
                if (response.status === 200) {
                    let result = JSON.parse(response.request.response);                    
                    // reset the form
                    self.setState({
                        event_name: "",
                        event_location: "",
                        event_date_time: JSON.stringify(new Date()).slice(1, 17),
                    })

                    // array @ 0 is list of events for group, array @1 is the user's attending events
                    // refresh the drawer (parent class)
                    self.props.updateParent(result[0], result[1]);


                    
                }
            })
            .catch(function (error) {
                console.log(error);
        });
    }
    
    static getDerivedStateFromProps(props, state){
        if(props.gid !== state.gid || props.gpp !== state.gpp){
           return { gid: props.gid, gpp: props.gpp};
       }
       else return null;
     }

    componentDidUpdate(props, state) {
        if(props.gid !== this.props.gid || props.gpp !== this.props.gpp){
          //Perform some operation here
            this.setState({
                gid: this.props.gid, 
                gpp: this.props.gpp
            });
        }
    }
    
    render(){
        const { classes } = this.props;
        console.log("[" + this.props.username + "] is in gid [" + this.state.gid + "], a [" + this.state.gpp + "] group")

        return(
            <form onSubmit={this.createEvent}>
                <div className={classes.textFields}>
                    <TextField 
                        className={classes.textField}
                        value={this.state.event_name}
                        label="Name"
                        variant="outlined"
                        onChange = {(e) => this.setState({event_name: e.target.value})}
                    />
                    <TextField
                        className={classes.textField}
                        value={this.state.event_location}
                        label="Location"
                        variant="outlined"
                        onChange = {(e) => this.setState({event_location: e.target.value})}
                    />
                </div>
                <div className={classes.textFields}>
                    <TextField
                        className={classes.textField}
                        id="datetime-local"
                        label="Date & Time"
                        type="datetime-local"
                        variant="outlined"
                        value={this.state.event_date_time}
                        onChange = {(e) => this.setState({event_date_time: e.target.value})}
                        InputLabelProps={{shrink: true}}
                    />
                </div>
                <div className={classes.textFields}>
                    <Button
                        variant="contained"
                        color="primary"
                        type="submit"
                        className={classes.button}
                        startIcon={<EventIcon/>}
                    >
                        Create
                    </Button>
                 </div>
            </form>
        );
    }

}
export default withStyles(styles)(CreateEvent);