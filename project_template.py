project_template = """
GameProjectClass {
    ID "DayZ"
    TITLE "DayZ"
    Configurations {
        GameProjectConfigClass PC {
            platformHardware PC
	        skeletonDefinitions "DZ/Anims/cfg/skeletons.anim.xml"
            FileSystem {
                FileSystemPathClass {
                    Name "Game Root"
                    Directory "./"
                }
                {0}
	        }
            imageSets {
                "gui/imagesets/ccgui_enforce.imageset"
                "gui/imagesets/rover_imageset.imageset"
                "gui/imagesets/dayz_gui.imageset"
                "gui/imagesets/dayz_crosshairs.imageset"
                "gui/imagesets/dayz_inventory.imageset"
                "gui/imagesets/inventory_icons.imageset"
                "gui/imagesets/main_menu_newsfeed.imageset"
                "gui/imagesets/smart_panel.imageset"
                "gui/imagesets/GUI_back_alpha.imageset"
                "gui/imagesets/GUI_back_alpha_icon.imageset"
                "gui/imagesets/xbox_buttons.imageset"
                "gui/imagesets/playstation_buttons.imageset"
                "gui/imagesets/selection.imageset"
                "gui/imagesets/console_toolbar.imageset"
                {1}
            }
            widgetStyles {
                "gui/looknfeel/dayzwidgets.styles" 
                "gui/looknfeel/widgets.styles"
                {2}
            }
            ScriptModules {
                ScriptModulePathClass {
                    Name "core"
                    Paths {
                        "scripts/1_Core"
                        {3}
                    }
                    EntryPoint ""
                }
                ScriptModulePathClass {
                    Name "gameLib"
                    Paths {
                        "scripts/2_GameLib"
                        {4}
                    }
                    EntryPoint ""
                }
                ScriptModulePathClass {
                    Name "game"
                    Paths {
                        "scripts/3_Game"
                        {5}
                    }
                    EntryPoint "CreateGame"
                }
                ScriptModulePathClass {
                    Name "world"
                    Paths {
                        "scripts/4_World"
                        {6}
                    }
                    EntryPoint ""
                }
                ScriptModulePathClass {
                    Name "mission"
                    Paths {
                        "scripts/5_Mission"
                        {7}
                    }
                    EntryPoint "CreateMission"
                }
                ScriptModulePathClass {
                    Name "workbench"
                    Paths {
                        "scripts/editor/Workbench"
                        "scripts/editor/plugins"
                        {8}
                    }
                    EntryPoint ""
                } 
            }
        }
        GameProjectConfigClass XBOX_ONE {
            platformHardware XBOX_ONE
        }
        GameProjectConfigClass PS4 {
            platformHardware PS4
        }
        GameProjectConfigClass LINUX {
            platformHardware LINUX
        }
    }
}

"""