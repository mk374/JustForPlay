import React from 'react';
import GroupLink from './GroupLink';
import CreateEvent from './CreateEvent';
import CreateGroup from './CreateGroup';

import Drawer from '@material-ui/core/Drawer';
import AddIcon from '@material-ui/icons/Add'
import Button from '@material-ui/core/Button';
import Fab from '@material-ui/core/Fab';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import { withStyles } from '@material-ui/styles';
import {fade} from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import SearchIcon from '@material-ui/icons/Search';
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
    },
    paper: {
        padding: 10,
        margin: 10,
        maxWidth: 700
    },
  });

class HomePage extends React.Component{
    constructor(props){
        super(props);       
        this.state={
            user : this.props.user,
            whoClicked: "",
            groups: this.props.groups,
            isOpen: false,
            group_name: "No Page Selected",
            group_community_id: "-1",
            group_description: "Empty Description", // these haven't been resolved
            group_public_private: "N/A",
            group_members: [],
            group_events: [],
            anchorEl: null,
        }
    }

    popPage = async(e, group_id, g_name, g_ci, g_description, g_pop) =>{
        e.preventDefault();
        // to change in the future for custom routing

            var apiBaseUrl = "http://35.202.227.79:5000/";
            var self = this;
            let userinfo={
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
                    console.log(result);
                    // set the the current states as such
                    self.setState({
                        group_members: result[0],
                        group_events: result[1],
                        group_name: g_name,
                        group_community_id: g_ci,
                        group_description: g_description,
                        group_public_private: g_pop,
                    });
                }
            })
            .catch(function (error) {
                console.log(error);
            });
        
        if(this.state.isOpen === false){
            this.toggleDrawer();
            this.setState({
                whoClicked: group_id
            });
        }else if(group_id !== this.state.whoClicked){
            this.setState({
                whoClicked: group_id
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

    updateParent = () => {
        // updating groups is gonna be a monster
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
        groupMembers.forEach(member => {
            groupMembersArr.push(<li>{member.uid}</li>);
        });

        var groupEvents = this.state.group_events;
        var groupEventsArr = [];
        groupEvents.forEach(event => {
            groupEventsArr.push(<li id={event.eventid}>{event.event_name}</li>);
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
                    <Fab color="primary" aria-label="add" onClick={(e) => this.setState({anchorEl: e.currentTarget})}>
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
                                <h1>{this.state.group_name}</h1>
                                <p>[DESCRIPTION] {this.state.group_description}</p>
                            </Paper>

                            <Paper className={classes.paper}>
                                <h3>Create Event</h3>
                                <CreateEvent username={this.state.user.name} gid={this.state.whoClicked} gpp={this.state.group_public_private}></CreateEvent>
                            </Paper>
                            
                            <Paper className={classes.paper}>
                                <h3>Members</h3>
                                    <ul>{groupMembersArr}</ul>
                            </Paper>
                                    
                            <Paper className={classes.paper}>
                                <h3>Events</h3>
                                    <ul>{groupEventsArr}</ul>
                            </Paper>

                        </div>
                </Drawer>
            
            </div>

        );
    }
}
export default withStyles(styles)(HomePage);