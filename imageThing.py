void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    vec2 xy = fragCoord.xy / iResolution.xy;
    vec4 texColor = texture2D(iChannel0,xy); // Get the pixel at xy from iChannel0
    vec4 webcam = texture2D(iChannel1,xy); // Get the pixel at xy from iChannel0
    texColor.r *= abs(sin(iGlobalTime));
    texColor.g = webcam.g;
    texColor.b *= abs(sin(iGlobalTime) * cos(iGlobalTime));
    texColor /= texture2D(iChannel2, xy); // Using a soundcloud channel!
    fragColor = texColor; // Set the screen pixel to that color
}
mainImage()
