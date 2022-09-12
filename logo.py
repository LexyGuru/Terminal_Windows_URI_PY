from sty import fg

class logos:
    @staticmethod
    def main_logo():
        logo_color_a: str
        logo_color_b: str
        logo_color_c: str
        logo_color_d: str
        logo_color_e: str
        logo_color_f: str
        logo_color_g: str
        logo_color_h: str
        logo_color_i: str

        logo_color_a = fg(200, 50, 80) + "                                                    (       )    " + fg.rs
        logo_color_b = fg(200, 60, 70) + "   (  (               (                             )\ ) ( /(    " + fg.rs
        logo_color_c = fg(200, 70, 60) + "   )\))(    (         )\ )    (  (         (  (  ( (()/( )\())   " + fg.rs
        logo_color_d = fg(200, 80, 50) + "  ((_)()\ ) )\  (    (()/( (  )\))(  (     )\ )( )\ /(_)((_)\    " + fg.rs
        logo_color_e = fg(200, 90, 40) + "  _(())\_)(((_) )\ )  ((_)))\((_)()\ )\ _ ((_(()((_(_))__ ((_)   " + fg.rs
        logo_color_f = fg(200, 100, 30) + "  \ \((_)/ /(_)_(_/(  _| |((__(()((_((_| | | |((_(_| _ \ \ / /   " + fg.rs
        logo_color_g = fg(200, 110, 20) + "   \ \/\/ / | |   \)/ _` / _ \ V  V (_-| |_| |  _| |  _/\ V /    " + fg.rs
        logo_color_h = fg(200, 120, 10) + "    \_/\_/  |_|_||_|\__,_\___/\_/\_//__/\___/|_| |_|_|   |_|     " + fg.rs
        logo_color_i = fg(200, 130, 0) + "                        Apps by LexyGuru                          " + fg.rs

        print(
            "\n" + logo_color_a + "\n" + logo_color_b + "\n" + logo_color_c + "\n" + logo_color_d + "\n" + logo_color_e + "\n" + logo_color_f + "\n" + logo_color_g + "\n" + logo_color_h + "\n" + logo_color_i + "\n")
