import React from 'react';
import GroupLink from './GroupLink';
import CreateEvent from './CreateEvent';
import CreateGroup from './CreateGroup';
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import Drawer from '@material-ui/core/Drawer';
import AddIcon from '@material-ui/icons/Add';
import RemoveIcon from '@material-ui/icons/Remove';
import PersonAddIcon from '@material-ui/icons/PersonAdd';
import PersonAddDisabledIcon from '@material-ui/icons/PersonAddDisabled';
import Button from '@material-ui/core/Button';
import Fab from '@material-ui/core/Fab';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import { withStyles } from '@material-ui/styles';
import {fade} from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import SearchIcon from '@material-ui/icons/Search';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore'; 
import InputBase from '@material-ui/core/InputBase';
import Paper from '@material-ui/core/Paper';
import Popover from '@material-ui/core/Popover'

import axios from 'axios';

const drawerWidth = 800;
const styles = theme => ({
    root: {
        display: 'flex',
        flexGrow: 1,
    },
    menuButton: {
        marginRight: '4px',
    },
    title: {
        display: 'block',
        fontWeight: '500'
    },
    spacer: {
        flexGrow: 1
    },
    search: {
        position: 'relative',
        borderRadius: '4px',
        padding: '5px',
        backgroundColor: fade('#ffffff', 0.15),
        '&:hover': {
          backgroundColor: fade('#ffffff', 0.25),
        },
        marginLeft: 0,
        width: '250px',
    },
    searchIcon: {
        width: '20px',
        position: 'absolute',
        pointerEvents: 'none',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        paddingLeft: '5px'
    },
    inputRoot: {
        color: 'inherit',
    },
    inputInput: {
        padding: '2px',
        width: '95%',
        '&:focus': {
            width: '100%',
        }
    },
    logout: {
        marginLeft: '10px'
    },
    divbyAndy: {
        padding: '10px 20px 40px 20px'
    },
    drawer: {
        width: drawerWidth,
        flexShrink: 0,
    },
    appBar: {
        position: 'relative',
        zIndex: 1400,
        backgroundColor: "#84c1ff"
    },
    paper: {
        padding: 10,
        margin: 10,
        maxWidth: 700
    },
    eventName:{
        marginLeft: 10,
        paddingTop: 6
    },
    joinEventButton:{
        backgroundColor: "#90ee90",
    },
    leaveEventButton:{
        backgroundColor: "#ff6961",
    },
    fabs: {
        backgroundColor: "#4998e6"
    },
    inline: {
        display: "inline-block",
        flexGrow: 1

    }
  });

class HomePage extends React.Component{
    constructor(props){
        super(props);       
        this.state={
            user : this.props.user,
            group_id: "",
            groups: this.props.groups,
            isOpen: false,
            group_name: "No Page Selected",
            group_community: "-1",
            group_description: "Empty Description", // these haven't been resolved
            group_public_private: "N/A",
            group_members: [],
            group_events: [],
            group_attending_events: [],
            anchorEl: null,
        }
    }

    updateGroups = (groups) => {
        this.setState({
            groups: groups
        })
    }
    updateEvents = (events, attending) => {
        console.log("UPDATING EVENTS:")
        console.log(events);
        console.log(attending);

        this.setState({
            group_events: events,
            group_attending_events: attending
        })
    }

    popPage = async(e, group_id, g_name, g_ci, g_description, g_pop) =>{
        e.preventDefault();
            // to change in the future for custom routing
            var apiBaseUrl = "http://35.202.227.79:5000/";
            var self = this;
            let userinfo={
                uid: this.state.user.uid,
                gid: group_id,
            };

            var config = {
                headers: {'Access-Control-Allow-Origin': '*'},
                withCredentials: false
            };

            // post it to the backends
            axios.post(apiBaseUrl+'get-group', userinfo, config).then(function (response) {
                if(response.status === 200){
                    let result = JSON.parse(response.request.response);
                    // set the the current states as such
                    self.setState({
                        group_members: result[0],
                        group_events: result[1],
                        group_attending_events: result[2],
                        group_name: g_name,
                        group_community: g_ci,
                        group_description: g_description,
                        group_public_private: g_pop,
                    });
                    console.log("PAGE POPULATED W/:")
                    console.log(self.state);
                }
            })
            .catch(function (error) {
                console.log(error);
            });
        
        if(this.state.isOpen === false){
            this.toggleDrawer();
            this.setState({
                group_id: group_id
            });
        }else if(group_id !== this.state.group_id){
            this.setState({
                group_id: group_id
            });
        }else{
            this.toggleDrawer();
        }

    }
    /* populate the drawer with data if clicked by other link then just change group*/
    toggleDrawer = () => {
        this.setState({
            isOpen: !this.state.isOpen
        });  
    };

    attendEvent = (e) => {
        e.preventDefault();
        var apiBaseUrl = "http://35.202.227.79:5000/";
            var self = this;
            let userinfo={
                uid: this.state.user.uid,
                eventid: e.currentTarget.value,
            };

            var config = {
                headers: {'Access-Control-Allow-Origin': '*'},
                withCredentials: false
            };

            // post it to the backends
            axios.post(apiBaseUrl+'add-attending', userinfo, config).then(function (response) {
                if(response.status === 200){
                    let result = JSON.parse(response.request.response);
                    self.setState({
                        group_attending_events: result
                    })
                    /* add snackbar to according things */
                }else{
                    /* throw error */
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    unattendEvent = (e) => {
        e.preventDefault();
        var apiBaseUrl = "http://35.202.227.79:5000/";
            var self = this;
            let userinfo={
                uid: this.state.user.uid,
                eventid: e.currentTarget.value,
            };

            var config = {
                headers: {'Access-Control-Allow-Origin': '*'},
                withCredentials: false
            };

            // post it to the backends
            axios.post(apiBaseUrl+'del-attending', userinfo, config).then(function (response) {
                if(response.status === 200){
                    let result = JSON.parse(response.request.response);
                    self.setState({
                        group_attending_events: result
                    })
                    /* add snackbar to according things */
                }else{
                    /* throw error */
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    }
    
    handleLeave = (e) => {
        e.preventDefault();
  
        var apiBaseUrl = "http://35.202.227.79:5000/";
        let userinfo = {
            gid: this.state.group_id,
            uid: this.state.user.uid,
        };  
        var config = {
            headers: {
                'Access-Control-Allow-Origin': '*'
            },
            withCredentials: false
        };
  
        axios.post(apiBaseUrl + "del-member", userinfo, config).then(function (response) {
          if (response.status === 200) {
              // reset the form
            }
        })
        .catch(function (error) {
            console.log(error);
        });
    }
    
    handleJoin = (e) => {
            e.preventDefault();
  
            var apiBaseUrl = "http://35.202.227.79:5000/";
            let userinfo = {
                gid: this.state.group_id,
                uid: this.state.user.uid,
            };
            
            var config = {
                headers: {
                    'Access-Control-Allow-Origin': '*'
                },
                withCredentials: false
            };
        
            axios.post(apiBaseUrl + "add-member", userinfo, config).then(function (response) {
            if (response.status === 200) {
                let result = JSON.parse(response.request.response);
                // reset the form
                this.setState({
                    userInGroup: !this.state.userInGroup
            })
        }
        })
        .catch(function (error) {
            console.log(error);
        });
    }

    render(){
        // not sure what this is lmao but this is what works
        const { classes } = this.props;
        
        // for create group popover
        const isOpen = Boolean(this.state.anchorEl);
        const id = isOpen ? 'simple-popover' : undefined;
      
        // generate the links
        var groupLinks = this.state.groups;
        var groupLinksArr = [];
        var count = 0;
        groupLinks.forEach(group => {
            groupLinksArr.push(<GroupLink key={count} group={group} onClick={this.popPage}></GroupLink>);
            count++;
        });

        var groupMembers = this.state.group_members;
        var groupMembersArr = [];
        var userInGroup = false;
        groupMembers.forEach(member => {
            userInGroup = member.uid === this.state.user.uid ? true : userInGroup;
            groupMembersArr.push(<li>{member.uid}</li>);
        });

        var groupEvents = this.state.group_events;
        var groupEventsArr = [];
        var groupAttendEventsArr = [];
        // split between my events and all group events
        groupEvents.forEach(event => {
            if(this.state.group_attending_events.includes(event.eventid)){
                groupAttendEventsArr.push(
                    <ExpansionPanel>
                        <ExpansionPanelSummary
                            expandIcon={<ExpandMoreIcon />}
                            aria-controls="panel1a-content"
                            id="panel1a-header"
                        >
                            <Button value={event.eventid} className={classes.leaveEventButton} onClick={this.unattendEvent}>
                                <RemoveIcon/> Leave
                            </Button>
                            <div className={classes.eventName}>
                                <Typography>{event.event_name}</Typography>
                            </div>
                        </ExpansionPanelSummary>
                        <ExpansionPanelDetails>
                            <div>
                                <ul>
                                    <li>Host: {event.host}</li>
                                    <li>Location: {event.location}</li>
                                    <li>Date: {event.e_date}</li>
                                    <li>Time: {event.e_time}</li>
                                </ul>
                            </div>
                        </ExpansionPanelDetails>
                    </ExpansionPanel>
                );
            }else{
                groupEventsArr.push(
                    <ExpansionPanel>
                        <ExpansionPanelSummary
                            expandIcon={<ExpandMoreIcon />}
                            aria-controls="panel1a-content"
                            id="panel1a-header"
                        >
                            <Button value={event.eventid} className={classes.joinEventButton} onClick={this.attendEvent}>
                                <AddIcon/> RSVP
                            </Button>
                            <div className={classes.eventName}>
                                <Typography>{event.event_name}</Typography>
                            </div>
                        </ExpansionPanelSummary>
                        <ExpansionPanelDetails>
                            <div>
                                <ul>
                                    <li>Host: {event.host}</li>
                                    <li>Location: {event.location}</li>
                                    <li>Date: {event.e_date}</li>
                                    <li>Time: {event.e_time}</li>
                                </ul>
                            </div>
                        </ExpansionPanelDetails>
                    </ExpansionPanel>
                );
            }
        });

        return(
            <div> 
                 <AppBar className={classes.appBar} position="static">
                    <Toolbar>
                    <Typography className={classes.title} variant="h4" noWrap>
                        <span role="img" aria-label="Woman With Bunny Ears">👯</span>
                        &nbsp; JustForPlay!
                    </Typography>
                    <div className={classes.spacer} />
                    <div className={classes.search}>
                        <div className={classes.searchIcon}>
                        <SearchIcon />
                        </div>
                        <InputBase
                        placeholder="Search…"
                        classes={{
                            root: classes.inputRoot,
                            input: classes.inputInput,
                        }}
                        inputProps={{ 'aria-label': 'search' }}
                        />
                    </div>
                    <Button onClick={this.props.onLogout} className={classes.logout} color="inherit">Logout</Button>
                    </Toolbar>
                </AppBar>
                <div align="left" className={classes.divbyAndy}> 
                    {groupLinksArr}
                </div>
                <div className={classes.divbyAndy}>
                    <Fab className={classes.fabs} color="primary" aria-label="add" onClick={(e) => this.setState({anchorEl: e.currentTarget})}>
                            <AddIcon />
                    </Fab>
                    <Popover
                        id={id}
                        open={isOpen}
                        anchorEl={this.state.anchorEl}
                        onClose={(e) => this.setState({anchorEl: null})}
                        anchorOrigin={{
                        vertical: 'bottom',
                        horizontal: 'center',
                        }}
                        transformOrigin={{
                        vertical: 'top',
                        horizontal: 'center',
                        }}
                    >
                        <CreateGroup uid={this.state.user.uid}>The content of the Popover.</CreateGroup>
                    </Popover>
                </div>
                
                <Drawer
                    className={classes.drawer}
                    variant="persistent"
                    anchor="right"
                    open={this.state.isOpen}
                    >
                        <div align="left" style={{paddingTop: '80px', paddingLeft: '25px', paddingRight: '25px'}}>
                            <Paper className={classes.paper}>
                                <div style={{display: "flex"}}>
                                <div className={classes.inline}><h1>{this.state.group_name}</h1></div>
                                <div className={classes.inline} align="right">
                                    <Button onClick={userInGroup ? this.handleLeave : this.handleJoin} className={userInGroup ? classes.leaveEventButton : classes.joinEventButton}>
                                        {userInGroup ? <PersonAddDisabledIcon/> : <PersonAddIcon/>} &nbsp; {userInGroup ? "Leave" : "Join"}
                                    </Button>
                                </div>
                                </div>
                                <p>{this.state.group_description}</p>
                            </Paper>

                            <Paper className={classes.paper}>
                                <h3>Create Event</h3>
                                <CreateEvent updateParent={this.updateEvents} uid={this.state.user.uid} username={this.state.user.name} gid={this.state.group_id} gpp={this.state.group_public_private}></CreateEvent>
                            </Paper>
                            
                            <Paper className={classes.paper}>
                                <h3>Members</h3>
                                    <ul>{groupMembersArr}</ul>
                            </Paper>

                            <Paper className={classes.paper}>
                                <h3>My Events</h3>
                                {groupAttendEventsArr}
                            </Paper>
     
                            <Paper className={classes.paper}>
                                <h3>Other Events</h3>
                                {groupEventsArr}
                            </Paper>
                        </div>
                </Drawer>
            
            </div>

        );
    }
}
export default withStyles(styles)(HomePage);