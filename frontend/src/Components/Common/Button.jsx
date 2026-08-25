import { Button } from "@mui/material";

const AppButton = ({
    children,
    variant = "contained",
    color = "primary",
    size = "medium",
    fullWidth = false,
    startIcon,
    endIcon,
    onClick,
    disabled = false,
    type = "button",
    sx = {}
}) => {

    return (
        <Button
            variant={variant}
            color={color}
            size={size}
            fullWidth={fullWidth}
            startIcon={startIcon}
            endIcon={endIcon}
            disabled={disabled}
            onClick={onClick}
            type={type}
            sx={{
                borderRadius: 2,
                px: 3,
                py: 1.2,
                fontWeight: 600,
                ...sx
            }}
        >
            {children}
        </Button>
    );
};

export default AppButton;