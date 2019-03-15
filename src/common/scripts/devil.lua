debug_print("Window Name: "..	get_window_name());
debug_print("Application name: "..get_application_name())

if (string.find(get_application_name(),".pdf")~=nil) then
    maximize();
end

-- if (string.find(get_window_name(),".docx")~=nil
-- 	or string.find(get_window_name(),".doc")~=nil
-- 	or string.find(get_window_name(),".pptx")~=nil
-- 	or string.find(get_window_name(),".ppt")~=nil
-- 	or string.find(get_window_name(),".xls")~=nil
-- 	or string.find(get_window_name(),".xlsx")~=nil) then
--     maximize();
-- end

if (string.find(get_application_name(),"LibreOffice")~=nil) then
    maximize();
end

if (get_application_name()=="gedit") then
	maximize();
end

-- if (get_application_name()=="libreoffice") then
-- 	maximize();
-- end

if (get_application_name()=="Image Viewer") then
	maximize();
end