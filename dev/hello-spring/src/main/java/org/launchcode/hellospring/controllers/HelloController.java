package org.launchcode.hellospring.controllers;


import org.apache.catalina.servlet4preview.http.HttpServletRequest;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
public class HelloController {

    @RequestMapping(value = "")
    @ResponseBody
    public String index(HttpServletRequest request) {
        String name = request.getParameter("name");


        if (name == null) {
            name = "World";
        }

        return "Hello " + name;
    }

    @RequestMapping(value = "hello", method = RequestMethod.GET)
    @ResponseBody
    public String helloForm() {

        String html = "<form method='post'>" +
                "<input type='text' name='name' />" +
                "<select name='language' />" +
                //     "input name='languauge' />" +
                "<option value=''>--Choose a Language--</option>" +
                "<option value='english'>English</option>" +
                "<option value='spanish'>Spanish</option>" +
                "<option value='german'>German</option>" +
                "<option value='french'>French</option>" +
                "<option value='russian'>Russian</option>" +
                "</select>"

                +
                "<input type='submit' value='Greet Me!' />" +
                "</form>";

        return html;

    }

    /**
     * @RequestMapping(value = "hello", method = RequestMethod.POST)
     * @ResponseBody public String helloPost(HttpServletRequest request) {
     * String name = request.getParameter("name");
     * <p>
     * return "Hello " + name;
     * }
     **/
    @RequestMapping(value = "hello/{name}")
    @ResponseBody
    public String helloUrlSegment(@PathVariable String name) {
        return "Hello " + name;

    }

    @RequestMapping(value = "hello", method = RequestMethod.POST)
    @ResponseBody
    public String createMessage(HttpServletRequest request) {
        String name = request.getParameter("name");
        String language = request.getParameter("language");

        String greeting = "Hello ";

        switch (language) {
            case "english":
                greeting = "Hello ";
                break;
            case "french":
                greeting = "Bonjour ";
                break;
            case "german":
                greeting = "Halo ";
                break;
            case "russian":
                greeting = "Privet ";
                break;
            case "spanish":
                greeting = "Hola ";
                break;
        }

        String message = greeting + name;

        return message;

    }


        @RequestMapping(value = "goodbye")
        public String goodbye () {

            return "redirect:/";
        }


}

