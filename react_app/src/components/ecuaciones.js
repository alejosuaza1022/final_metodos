import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import Link from '@mui/material/Link';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import TimelineIcon from '@mui/icons-material/Timeline';
import Typography from '@mui/material/Typography';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { FormControl, InputLabel, MenuItem, Select, TextField } from '@mui/material';
import { URL } from "../config/vars";
import axios from "axios";
import Swal from "sweetalert2";

function Copyright(props) {


    return (
        <Typography variant="body2" color="#000" align="center" {...props}>
            {'Copyright © '}
            <Link color="inherit" href="https://mui.com/">
                Alejandro Suaza - Juan Mejia
            </Link>{' '}
            {new Date().getFullYear()}
            {'.'}
        </Typography>
    );
}

const theme = createTheme();

export default function Ecuaciones() {


    const [open, setOpen] = React.useState(false);

    const handleChange = (event) => {
        settype(event.target.value);
    };

    const handleClose = () => {
        setOpen(false);
    };

    const handleOpen = () => {
        setOpen(true);
    };


    const [type, settype] = React.useState('');
    const [x, setX] = React.useState('');
    const [y, setY] = React.useState('');
    const [dydx, setDydx] = React.useState('');
    const [h, setH] = React.useState('');
    const [xi, setXi] = React.useState('');
    const [xf, setXf] = React.useState('');
    const [result, setResult] = React.useState('');


    const resolveProblem = () => {

        if (x === "" || y === "" || dydx === "" || h === "" || xi === "" || xi === "" || type === "") {
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Debes de llenar todos los campos',
            })
        }
        axios.post((URL + '/' + type), {
            x, y, f: dydx, h, xi, xf
        })
            .then(function (response) {
                setResult(response.data)
            }).catch(
                function (error) {
                    Swal.fire({
                        icon: 'error',
                        title: 'Oops...',
                        text: 'Revisa los parametros',
                    })
                }
            )
    }



    return (
        <ThemeProvider theme={theme}>
            <Grid container component="main" sx={{ height: '100vh' }}>
                <CssBaseline />
                <Grid
                    item
                    xs={false}
                    sm={4}
                    md={5}
                    sx={{
                        backgroundImage: 'url(https://images.pexels.com/photos/6238048/pexels-photo-6238048.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940)',
                        backgroundRepeat: 'no-repeat',
                        backgroundColor: (t) =>
                            t.palette.mode === 'light' ? t.palette.grey[50] : t.palette.grey[900],
                        backgroundSize: 'cover',
                        backgroundPosition: 'center',
                    }}
                />
                <Grid item xs={12} sm={8} md={7} component={Paper} elevation={6} square>
                    <Box
                        sx={{
                            my: 8,
                            mx: 4,
                            display: 'flex',
                            flexDirection: 'column',
                            alignItems: 'center',
                        }}
                    >
                        <Avatar sx={{ m: 1, bgcolor: '#000' }}>
                            <TimelineIcon />
                        </Avatar>
                        <Typography component="h1" variant="h5">
                            Ecuaciones diferenciales
                        </Typography>
                        <Box component="form" noValidate sx={{ mt: 1 }}>
                            <InputLabel id="demo-simple-select-label">Seleccione tipo de metodo a usar</InputLabel>

                            <FormControl
                                fullWidth
                                color="primary"
                            >
                                <InputLabel id="demo-controlled-open-select-label">Tipo</InputLabel>
                                <Select
                                    labelId="demo-controlled-open-select-label"
                                    id="demo-controlled-open-select"
                                    open={open}
                                    onClose={handleClose}
                                    onOpen={handleOpen}
                                    value={type}
                                    label="Tipo"
                                    onChange={handleChange}
                                    color="primary"
                                >
                                    <MenuItem value={"rk-4"}>Runge-kutta 4to orden</MenuItem>
                                    <MenuItem value={"rk-orden-superior"}>Runge-kutta orden superior</MenuItem>
                                </Select>

                                <TextField
                                    margin="normal"
                                    required
                                    fullWidth

                                    value={x} onChange={(e) => { setX(e.target.value) }} label="X" color="primary" focused
                                />
                                <TextField
                                    margin="normal"
                                    required
                                    fullWidth
                                    autoFocus
                                    value={y} onChange={(e) => { setY(e.target.value) }} label="Y" color="primary" focused
                                />
                                <TextField
                                    margin="normal"
                                    required
                                    fullWidth
                                    autoFocus
                                    value={dydx} onChange={(e) => { setDydx(e.target.value) }} label="Función" color="primary" focused
                                />
                                <TextField
                                    margin="normal"
                                    required
                                    fullWidth
                                    autoFocus
                                    value={h} onChange={(e) => { setH(e.target.value) }} label="h" color="primary" focused
                                />
                                <TextField
                                    margin="normal"
                                    required
                                    fullWidth
                                    autoFocus
                                    value={xi} onChange={(e) => { setXi(e.target.value) }} label="XI" color="primary" focused
                                />
                                <TextField
                                    margin="normal"
                                    required
                                    fullWidth
                                    autoFocus
                                    value={xf} onChange={(e) => { setXf(e.target.value) }} label="XF" color="primary" focused
                                />

                                <Button

                                    fullWidth
                                    variant="contained"
                                    sx={{ mt: 3, mb: 2, bgcolor: '#000' }}
                                    onClick={resolveProblem}
                                >
                                    Resolver
                                </Button>
                               
                                <Button
                                    fullWidth
                                    variant="contained"
                                    color="primary"
                                    onClick={() => { window.location.reload();}}
                                >
                                    Limpiar
                                </Button>

                            </FormControl>

                            {
                                result != "" ?

                                    <div>
                                        <h3>Resultado:</h3>

                                        <TextField
                                            margin="normal"
                                            required
                                            fullWidth
                                            autoFocus
                                            placeholder="Result"
                                            multiline
                                            value={"x:[ " + result.x + " ] y:[ " + result.y + " ]"}
                                            rows={2}
                                            rowsMax={4}
                                            focused
                                        />

                                        <Box
                                            component="img"
                                            fullWidth
                                            sx={{
                                                height: 400,

                                            }}
                                            src={result.link} />
                                    </div>
                                    :

                                    <div />
                            }
                            <Copyright sx={{ mt: 5 }} />
                        </Box>
                    </Box>
                </Grid>
            </Grid>
        </ThemeProvider>
    );
}
