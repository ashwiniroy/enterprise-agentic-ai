import { createTheme } from "@mui/material/styles";

const theme = createTheme({

    palette:{

        mode:"light",

        primary:{
            main:"#2563EB"
        },

        secondary:{
            main:"#0EA5E9"
        },

        success:{
            main:"#16A34A"
        },

        warning:{
            main:"#F59E0B"
        },

        error:{
            main:"#DC2626"
        },

        background:{
            default:"#F8FAFC",
            paper:"#FFFFFF"
        },

        text:{
            primary:"#1E293B",
            secondary:"#64748B"
        }

    },

    typography:{

        fontFamily:[
            "Inter",
            "Roboto",
            "sans-serif"
        ].join(","),

        h4:{
            fontWeight:700
        },

        h5:{
            fontWeight:600
        },

        h6:{
            fontWeight:600
        },

        button:{
            textTransform:"none",
            fontWeight:600
        }

    },

    shape:{
        borderRadius:10
    }

});

export default theme;