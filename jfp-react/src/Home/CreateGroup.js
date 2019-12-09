import React from 'react';
import TextField from '@material-ui/core/TextField';
import GroupAddIcon from '@material-ui/icons/GroupAdd';
import Button from '@material-ui/core/Button';
import Checkbox from '@material-ui/core/Checkbox';
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
        paddingRight: 5
    },
    spaneth: {
        paddingRight: 140
    },
    title: {
        paddingTop: 20,
        paddingLeft: 20
    }
  });

class CreateGroup extends React.Component {
    constructor(props){
        super(props);
        this.state={
            uid : this.props.uid,
            g_name: "",
            g_community: "",
            g_zip: "",
            g_description: "",
            g_pop: "private",
        }
    }

    createGroup = (e) =>{
        e.preventDefault();

        var apiBaseUrl = "http://35.202.227.79:5000/";
        var self = this;
        
        /* POPULATE */
        let userinfo = {
            uid: this.state.uid,
            admin: true,
            group_name: this.state.g_name,
            community: this.state.g_community,
            zip_code: this.state.g_zip,
            public_or_private: this.state.g_pop,
            description: this.state.g_description,
        };

        console.log(userinfo);

        var config = {
            headers: {
                'Access-Control-Allow-Origin': '*'
            },
            withCredentials: false
        };
        // post it to the backends
        axios.post(apiBaseUrl + 'add-group', userinfo, config).then(function (response) {
                if (response.status === 200) {
                    // reset the form
                    self.setState({
                        g_name: "",
                        g_community: "",
                        g_zip: "",
                        g_description: "",
                    })

                    // reset the parent page: add snackbar
                    
                }
            })
            .catch(function (error) {
                console.log(error);
        });
    }
    
    render(){
        const { classes } = this.props;

        return(
        <div>
            <div className={classes.title}>
                <h2>Create Group</h2>
            </div>
            <form onSubmit={this.createGroup}>
                <div  className={classes.paper}>
                    <TextField 
                        className={classes.textField}
                        label="Group Name"
                        variant="outlined"
                        onChange = {(e) => this.setState({g_name: e.target.value})}
                    />
                </div>
                <div  className={classes.paper}>
                    <TextField
                        className={classes.textField}
                        label="Community"
                        variant="outlined"
                        onChange = {(e) => this.setState({g_community: e.target.value})}
                    />
                    <TextField
                        className={classes.textField}
                        label="Zip Code"
                        type="text"
                        pattern="[0-9]{5}"
                        variant="outlined"
                        onChange = {(e) => this.setState({g_zip: e.target.value})}
                    />
                </div>
                <div className={classes.paper}>
                    <TextField
                        id="outlined-multiline-static"
                        label="Description"
                        multiline
                        rows="3"
                        variant="outlined"
                        onChange = {(e) => this.setState({g_description: e.target.value})}
                    />
                    
                </div>
                <div className={classes.paper}>
                    <span className={classes.spaneth}>
                        <Checkbox
                            onChange={(e) => this.setState({g_pop: this.state.g_pop === e.target.value ? "public" : e.target.value})}
                            value = "private" />
                        <label>Private</label>
                    </span>
                    <Button
                        variant="contained"
                        color="primary"
                        type="submit"
                        className={classes.button}
                        startIcon={<GroupAddIcon/>}
                    >
                        Create Group
                    </Button>
                 </div>
            </form>
        </div>
        );
    }

}
export default withStyles(styles)(CreateGroup);