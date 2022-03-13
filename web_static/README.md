# 0x01. AirBnB clone - Web static
## Details
      By Guillaume          Weight: 1                Ongoing project - started 03-10-2022, must end by 03-13-2022 (in about 5 hours)          - you're done with 33% of tasks.      Manual QA review must be done          (request it when you are done with the project)       ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2021/9/135ef103cf7ed150c9760aadc66844113dfc3d35.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220312%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220312T234943Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5426e5dfb0ff7109ee8f18484e075ab024634f98d39da5e2694e01e645e012ee) 

## Background Context
### Web static, what?
Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!
Before developing a big and complex web application, we will build the front end step-by-step. 
The first step is to “design” / “sketch” / “prototype” each element:
* Create simple HTML static pages
* Style guide
* Fake contents
* No Javascript
* No data loaded from anything
During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.
Before starting, please fork or clone the repository   ` AirBnB_clone `   from your partner if you were not the owner of the previous project.
## Resources
Read or watch :
* [Learn to Code HTML & CSS](https://intranet.hbtn.io/rltoken/qq7qrSgdVRuD1kPd_jf7Fw) 
 (until “Creating Lists” included)
* [Inline Styles in HTML](https://intranet.hbtn.io/rltoken/xW69RnLZMt3AusI1SDvr8g) 

* [Specifics on CSS Specificity](https://intranet.hbtn.io/rltoken/sO3wz-QbhwYdKJqvokC4PA) 

* [CSS SpeciFishity](https://intranet.hbtn.io/rltoken/NvqQf3dgY64bb-QWC5Cueg) 

* [Introduction to HTML](https://intranet.hbtn.io/rltoken/STaxnOI5qv1enUuwIALelw) 

* [CSS](https://intranet.hbtn.io/rltoken/g-uj9Azx1rALX49xCZHK0w) 

* [MDN](https://intranet.hbtn.io/rltoken/El1BHRNNO2hPEcOt_XwF-Q) 

* [center boxes](https://intranet.hbtn.io/rltoken/HI0qRNDq20cgICIhO18kUQ) 

## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/O8BWXDOfoda19l0QdcprUg) 
 ,  without the help of Google :
### General
* What is HTML
* How to create an HTML page
* What is a markup language
* What is the DOM
* What is an element / tag
* What is an attribute
* How does the browser load a webpage
* What is CSS
* How to add style to an element
* What is a class
* What is a selector
* How to compute CSS Specificity Value
* What are Box properties in CSS
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files should end with a new line
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Your code should be W3C compliant and validate with [W3C-Validator](https://intranet.hbtn.io/rltoken/4dtXqWSyIeSCFVqQ9Eo6NA) 

* All your CSS files should be in  ` styles `  folder
* All your images should be in  ` images `  folder
* You are not allowed to use  ` !important `  and  ` id `  ( ` #... `  in the CSS file)
* You are not allowed to use tags  ` img ` ,  ` embed `  and  ` iframe ` 
* You are not allowed to use Javascript
* Current screenshots have been done on  ` Chrome 56 `  or more. 
* No cross browsers 
* You have to follow all requirements but some  ` margin ` / ` padding `  are missing - you should try to fit as much as you can to screenshots
## More Info
 ![](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step1.png) 

## Quiz questions
Show
#### 
        
        Question #0
    
 Quiz question Body Is the following HTML markup valid? 
 ` <html></html>
 ` (elements are correctly tagged, we don’t care about   ` !Doctype `   here)
 Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #1
    
 Quiz question Body Is the following HTML markup valid? 
 ` <html>
    <head>
    </head>
    <body>
    </body>
</html>
 ` (elements are correctly tagged, we don’t care about   ` !Doctype `   here)
 Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #2
    
 Quiz question Body Is the following HTML markup valid? 
 ` <html>
    <head>
    </head>
    <body>
    <body>
</html>
 ` (elements are correctly tagged, we don’t care about   ` !Doctype `   here)
 Quiz question Answers * Yes

* No

 Quiz question Tips #### Tips:
Each HTML tag must be closed
#### 
        
        Question #3
    
 Quiz question Body Is the following HTML markup valid? 
 ` <html>
    <head>
    </head>
    <body>
        <img src="logo.png" />
    </body>
</html>
 ` (elements are correctly tagged, we don’t care about   ` !Doctype `   here)
 Quiz question Answers * Yes

* No

 Quiz question Tips #### Tips:
 ` <img /> `   is an empty element
#### 
        
        Question #4
    
 Quiz question Body Is the following HTML markup valid? 
 ` <html>
    <head>
    </head>
    <body>
        <h1>Best <b>School</h1></b>
    </body>
</html>
 ` (elements are correctly tagged, we don’t care about   ` !Doctype `   here)
 Quiz question Answers * Yes

* No

 Quiz question Tips #### Tips:
“Always close something before opening a new thing”
#### 
        
        Question #5
    
 Quiz question Body Is the following HTML markup valid? 
```bash
<html>
    <head>
    </head>
    <body>
        <h1>
            <a href="www.google.com'>Google</a>
        </h1>
    </body>
</html>

```
(elements are correctly tagged, we don’t care about   ` !Doctype `   here)
 Quiz question Answers * Yes

* No

 Quiz question Tips #### Tips:
Number of quotes is important!
#### 
        
        Question #6
    
 Quiz question Body Is the following HTML markup valid? 
```bash
<html>
    <head>
    </head>
    <body>
        <h1>
            <a href="www.google.com">Go to <b>Google</b>
        </h1>
    </body>
</html>

```
(elements are correctly tagged, we don’t care about   ` !Doctype `   here)
 Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #7
    
 Quiz question Body Is following CSS syntax valid? 
 ` body {
    color: #FF0000;
}
 `  Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #8
    
 Quiz question Body Is following CSS syntax valid? 
 ` body {
    color: #FF0000;
}

* {
    font-size: 14px;
}
 `  Quiz question Answers * Yes

* No

 Quiz question Tips #### Tips:
[Universal selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Universal_selectors) 

#### 
        
        Question #9
    
 Quiz question Body Is following CSS syntax valid? 
```bash
body {
    color: #FF0000;
}

* {
    font-size: 14px;
    font-weight: 400
    text-align: center;
}

```
 Quiz question Answers * Yes

* No

 Quiz question Tips #### Tips:
Betty for CSS!
#### 
        
        Question #10
    
 Quiz question Body Is following CSS syntax valid? 
```bash
body {
    color: #FF0000;
}

* {
    font-size: 14px;
    text-align: center;

    h1 {
        margin: 30px;
    }
}

```
 Quiz question Answers * Yes

* No

 Quiz question Tips #### Tips:
CSS vs SCSS
#### 
        
        Question #11
    
 Quiz question Body Is following CSS syntax valid? 
```bash
body {
    color: #FF0000;
}

* {
    font-size: 14px;
    text-align: center;
    margin: 30px 12px 4px;
}

```
 Quiz question Answers * Yes

* No

 Quiz question Tips #### Tips:
 ` margin `   and   ` padding `   support 4 different syntaxes:  [margin](https://developer.mozilla.org/en-US/docs/Web/CSS/margin) 

#### 
        
        Question #12
    
 Quiz question Body Is following CSS syntax valid? 
 ` body {
    color: #FF0000;
}

h1.title {
    font-size: 16px;
}
 `  Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #13
    
 Quiz question Body Is following CSS syntax valid? 
 ` body {
    color: #FF0000;
}

div.filters h2 {
    font-size: 16px;
}
 `  Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #14
    
 Quiz question Body Is following CSS syntax valid? 
 ` body {
    color: #FF0000;
}

div.filters p.title h2 span.text.big {
    font-size: 20px;
}
 `  Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #15
    
 Quiz question Body Is following CSS syntax valid? 
```bash
body {
    color: #FF0000;
}

h3,
div.full_text,
div.small_text h4,
div.filters p.title {
    font-size: 20px;
}

```
 Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #16
    
 Quiz question Body Is following CSS syntax valid? 
```bash
body {
    color: #FF0000;
}

h3,
div.full_text
div.small_text h4
div.filters p.title {
    font-size: 20px;
}

```
 Quiz question Answers * Yes

* No

 Quiz question Tips #### Tips:
 ` , `   separates multiple selector, without it’s specific selector
#### 
        
        Question #17
    
 Quiz question Body In the following code, is the text   ` Best School `   red?
css:
 ` h1 {
    color: red;
}
 ` html:
 ` <h1>Best School</h1>
 `  Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #18
    
 Quiz question Body In the following code, is the text   ` Best School `   red?
css:
 ` h2 {
    color: red;
}
 ` html:
 ` <h1>Best School</h1>
 `  Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #19
    
 Quiz question Body In the following code, is the text   ` Best School `   red?
css:
 ` h1.title {
    color: red;
}
 ` html:
 ` <h1>Best School</h1>
 `  Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #20
    
 Quiz question Body In the following code, is the text   ` Best School `   red?
css:
 ` h1 div.title {
    color: red;
}
 ` html:
 ` <h1>Best School</h1>
 `  Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #21
    
 Quiz question Body In the following code, is the text   ` Best School `   red?
css:
 ` h3 span.text,
h1,
div.title {
    color: red;
}
 ` html:
 ` <h1>Best School</h1>
 `  Quiz question Answers * Yes

* No

 Quiz question Tips #### 
        
        Question #22
    
 Quiz question Body In the following code, is the text   ` Best School `   red?
css:
 ` h1 {
    color: green;
}

span.my_title {
    color: red;
}
 ` html:
 ` <h1>
    <span class="my_title">Best School</span>
</h1>
 `  Quiz question Answers * Yes

* No

 Quiz question Tips #### Tips:
[CSS selector math](http://www.standardista.com/wp-content/uploads/2012/01/specificity3.pdf) 

#### 
        
        Question #23
    
 Quiz question Body In the following code, is the text   ` Best School `   red?
css:
 ` h1 .my_title {
    color: green;
}

.my_title {
    color: red;
}
 ` html:
 ` <h1>
    <span class="my_title">Best School</span>
</h1>
 `  Quiz question Answers * Yes

* No

 Quiz question Tips #### Tips:
[CSS selector math](http://www.standardista.com/wp-content/uploads/2012/01/specificity3.pdf) 

## Tasks
### 0. Inline styling
          mandatory         Progress vs Score  Task Body Write an HTML page that displays a header and a footer.
Layout:
* Body:* no margin
* no padding

* Header:* color #FF0000 (red)
* height: 70px
* width: 100%

* Footer:* color #00FF00 (green)
* height: 60px
* width: 100%
* text  ` Best School `  center vertically and horizontally
* always at the bottom at the page

Requirements:
* You must use the  ` header `  and  ` footer `  tags
* You are not allowed to import any files
* You are not allowed to use the  ` style `  tag in the  ` head `  tag
* Use inline styling for all your tags
 ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2021/12/9b4481f4cfe46adc8fbf48e31c0b24236f597653.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220312%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220312T234943Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=95e65e71a5652dbedf450a8da3025c74d7c09dfab5daf5cb0ac7726744191704) 

 Task URLs  Github information Repo:
* GitHub repository:  ` AirBnB_clone ` 
* Directory:  ` web_static ` 
* File:  ` 0-index.html ` 
 Self-paced manual review  Panel footer - Controls 
### 1. Head styling
          mandatory         Progress vs Score  Task Body Write an HTML page that displays a header and a footer by using the   ` style `   tag in the   ` head `   tag (same as   ` 0-index.html `  )
Requirements:
* You must use the  ` header `  and  ` footer `  tags
* You are not allowed to import any files
* No inline styling
* You must use the  ` style `  tag in the  ` head `  tag
The layout must be exactly the same as   ` 0-index.html ` 
 Task URLs  Github information Repo:
* GitHub repository:  ` AirBnB_clone ` 
* Directory:  ` web_static ` 
* File:  ` 1-index.html ` 
 Self-paced manual review  Panel footer - Controls 
### 2. CSS files
          mandatory         Progress vs Score  Task Body Write an HTML page that displays a header and a footer by using CSS files (same as   ` 1-index.html `  )
Requirements:
* You must use the  ` header `  and  ` footer `  tags
* No inline styling
* You must have 3 CSS files:*  ` styles/2-common.css ` : for global style (i.e. the  ` body `  style)
*  ` styles/2-header.css ` : for header style
*  ` styles/2-footer.css ` : for footer style

The layout must be exactly the same as   ` 1-index.html ` 
 Task URLs  Github information Repo:
* GitHub repository:  ` AirBnB_clone ` 
* Directory:  ` web_static ` 
* File:  ` 2-index.html, styles/2-common.css, styles/2-header.css, styles/2-footer.css ` 
 Self-paced manual review  Panel footer - Controls 
### 3. Zoning done!
          mandatory         Progress vs Score  Task Body Write an HTML page that displays a header and footer by using CSS files (same as   ` 2-index.html `  )
Layout:
* Common:* no margin
* no padding
* font color: #484848
* font size: 14px
* font family:  ` Circular,"Helvetica Neue",Helvetica,Arial,sans-serif; ` 
* [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon.png) 
 in the browser tab

* Header:* color: white
* height: 70px
* width: 100%
* border bottom 1px #CCCCCC
* [logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/logo.png) 
 align on left and center vertically (20px space at the left)

* Footer:* color white
* height: 60px
* width: 100%
* border top 1px #CCCCCC
* text  ` Best School `  center vertically and horizontally
* always at the bottom at the page

Requirements:
* No inline style
* You are not allowed to use the  ` img `  tag
* You are not allowed to use the  ` style `  tag in the  ` head `  tag
* All images must be stored in the  ` images `  folder
* You must have 3 CSS files:*  ` styles/3-common.css ` : for the global style (i.e  ` body `  style)
*  ` styles/3-header.css ` : for the header style
*  ` styles/3-footer.css ` : for the footer style

 ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2021/12/14f2c84c49affbb865ff84a3292d2e76a211993c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220312%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220312T234943Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6202a93845c66e8f9d831098780d4f5f0dba6aba033c5fb0155d0cf881cba9fe) 

 Task URLs  Github information Repo:
* GitHub repository:  ` AirBnB_clone ` 
* Directory:  ` web_static ` 
* File:  ` 3-index.html, styles/3-common.css, styles/3-header.css, styles/3-footer.css, images/ ` 
 Self-paced manual review  Panel footer - Controls 
### 4. Search!
          mandatory         Progress vs Score  Task Body Write an HTML page that displays a header, footer and a filters box with a search button.
Layout: (based on   ` 3-index.html `  )
* Container:* between  ` header `  and  ` footer `  tags, add a  ` div ` :* classname:  ` container ` 
* max width 1000px
* margin top and bottom 30px - it should be 30px under the bottom of the  ` header `  (screenshot)
* center horizontally


* Filter section: * tag  ` section ` 
* classname  ` filters ` 
* inside the  ` .container ` 
* color white
* height: 70px
* width: 100% of the container
* border 1px #DDDDDD with radius 4px

* Button search:* tag  ` button ` 
* text  ` Search ` 
* font size: 18px
* inside the section filters
* background color #FF5A5F
* text color #FFFFFF
* height: 48px
* width: 20% of the section filters
* no borders
* border radius: 4px
* center vertically and at 30px of the right border
* change opacity to 90% when the mouse is on the button

Requirements:
* You must use:  ` header ` ,  ` footer ` ,  ` section ` ,  ` button `  tags
* No inline style
* You are not allowed to use the  ` img `  tag
* You are not allowed to use the  ` style `  tag in the  ` head `  tag
* All images must be stored in the  ` images `  folder
* You must have 4 CSS files:*  ` styles/4-common.css ` : for the global style ( ` body `  and  ` .container `  styles)
*  ` styles/3-header.css ` : for the header style
*  ` styles/3-footer.css ` : for the footer style
*  ` styles/4-filters.css ` : for the filters style

*  ` 4-index.html ` won’t be W3C valid, don’t worry, it’s temporary
 ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2021/12/3798a756663ec485f194f5c5e1b55b15326174f3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220312%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220312T234943Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=5a669fe524f4e8a3e361a550323556ee18b1d6d105a761580a49dbc2a1284eac) 

 Task URLs  Github information Repo:
* GitHub repository:  ` AirBnB_clone ` 
* Directory:  ` web_static ` 
* File: ```bash
4-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/4-filters.css, images/
```

 Self-paced manual review  Panel footer - Controls 
### 5. More filters
          mandatory         Progress vs Score  Task Body Write an HTML page that displays a header, footer and a filters box.
Layout: (based on   ` 4-index.html `  )
* Locations and Amenities filters:* tag:  ` div ` 
* classname:  ` locations `  for location tag and  ` amenities `  for the other
* inside the section filters (same level as the  ` button `  Search)
* height: 100% of the section filters
* width: 25% of the section filters
* border right #DDDDDD 1px only for the first left filter
* contains a title:* tag:  ` h3 ` 
* font weight: 600
* text  ` States `  or  ` Amenities ` 

* contains a subtitle:* tag:  ` h4 ` 
* font weight: 400
* font size: 14px
* text with fake contents


Requirements:
* You must use:  ` header ` ,  ` footer ` ,  ` section ` ,  ` button ` ,  ` h3 ` ,  ` h4 `  tags
* No inline style
* You are not allowed to use the  ` img `  tag
* You are not allowed to use the  ` style `  tag in the  ` head `  tag
* All images must be stored in the  ` images `  folder
* You must have 4 CSS files:*  ` styles/4-common.css ` : for the global style ( ` body `  and  ` .container `  styles)
*  ` styles/3-header.css ` : for the header style
*  ` styles/3-footer.css ` : for the footer style
*  ` styles/5-filters.css ` : for the filters style

 ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2021/12/66ddfafd5fd59f06be3d55ea96cc6ad11a7f1ca9.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220312%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220312T234943Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c3bd66309e28c35caa9aac2d1767202fdcb258d6b7e31abb2923f37d6fd0e334) 

 Task URLs  Github information Repo:
* GitHub repository:  ` AirBnB_clone ` 
* Directory:  ` web_static ` 
* File: ```bash
5-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/5-filters.css, images/
```

 Self-paced manual review  Panel footer - Controls 
### 6. It's (h)over
          mandatory         Progress vs Score  Task Body Write an HTML page that displays a header, footer and a filters box with dropdown.
Layout: (based on   ` 5-index.html `  )
* Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter  ` div ` : * tag  ` ul ` 
* classname  ` popover ` 
* text should be fake now
* inside each  ` div ` 
* not displayed by default
* color #FAFAFA
* width same as the  ` div `  filter
* border #DDDDDD 1px with border radius 4px
* no list display
* Location filter has 2 levels of  ` ul ` / ` li ` :* state -> cities
* state name must be display in a  ` h2 `  tag (font size 16px)


Requirements:
* You must use:  ` header ` ,  ` footer ` ,  ` section ` ,  ` button ` ,  ` h3 ` ,  ` h4 ` ,  ` ul ` ,  ` li `  tags
* No inline style
* You are not allowed to use the  ` img `  tag
* You are not allowed to use the  ` style `  tag in the  ` head `  tag
* All images must be stored in the  ` images `  folder
* You must have 4 CSS files:*  ` styles/4-common.css ` : for the global style ( ` body `  and  ` .container `  styles)
*  ` styles/3-header.css ` : for the header style
*  ` styles/3-footer.css ` : for the footer style
*  ` styles/6-filters.css ` : for the filters style

 ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2021/12/36dd43123192ce96110b28c8a23ea9fbf851da0c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220312%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220312T234943Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=13ded8a3e843f4914f83f694ad9b5ba07ba7bdbee2e03dd8702a72e2c4922d64) 
  ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2021/12/9867494d8697023e5f50a90871003ac55e95eedb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220312%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220312T234943Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0b9ac1f39c645b983c73fb47e38c063d1fddaa33a0168fb10a70cac7c84f5b04) 

 Task URLs  Github information Repo:
* GitHub repository:  ` AirBnB_clone ` 
* Directory:  ` web_static ` 
* File: ```bash
6-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, images/
```

 Self-paced manual review  Panel footer - Controls 
### 7. Display results
          mandatory         Progress vs Score  Task Body Write an HTML page that displays a header, footer, a filters box with dropdown and results.
Layout: (based on   ` 6-index.html `  )
* Add Places section:* tag:  ` section ` 
* classname:  ` places ` 
* same level as the filters section, inside  ` .container ` 
* contains a title:* tag:  ` h1 ` 
* text:  ` Places ` 
* align in the top left
* font size: 30px

* contains multiple “Places” as listing (horizontal or vertical) describe by:* tag:  ` article ` 
* width: 390px
* padding and margin 20px
* border #FF5A5F 1px with radius 4px
* contains the place name:* tag:  ` h2 ` 
* font size: 30px
* center horizontally



Requirements:
* You must use:  ` header ` ,  ` footer ` ,  ` section ` ,  ` article ` ,  ` button ` ,  ` h1 ` ,  ` h2 ` ,  ` h3 ` ,  ` h4 ` ,  ` ul ` ,  ` li `  tags
* No inline style
* You are not allowed to use the  ` img `  tag
* You are not allowed to use the  ` style `  tag in the  ` head `  tag
* All images must be stored in the  ` images `  folder
* You must have 5 CSS files:*  ` styles/4-common.css ` : for the global style (i.e.  ` body `  and  ` .container `  styles)
*  ` styles/3-header.css ` : for the header style
*  ` styles/3-footer.css ` : for footer style
*  ` styles/6-filters.css ` : for the filters style
*  ` styles/7-places.css ` : for the places style

 ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2021/12/cb69b56a70528eeb3c52b4f0154a64b3f68d4fb6.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220312%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220312T234944Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=964979d111c14ce051d270c18d008c856cfcdf584b0dca01a919eb9979cdbc24) 

 Task URLs  Github information Repo:
* GitHub repository:  ` AirBnB_clone ` 
* Directory:  ` web_static ` 
* File: ```bash
7-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/7-places.css, images/
```

 Self-paced manual review  Panel footer - Controls 
### 8. More details
          mandatory         Progress vs Score  Task Body Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.
Layout: (based on   ` 7-index.html `  )
Add more information to a Place   ` article `  :
* Price by night:* tag:  ` div ` 
* classname:  ` price_by_night ` 
* same level as the place name
* font color: #FF5A5F
* border: #FF5A5F 4px rounded
* min width: 60px
* height: 60px
* font size: 30px
* align: the top right (with space)

* Information section:* tag:  ` div ` 
* classname:  ` information ` 
* height: 80px
* border: top and bottom #DDDDDD 1px
* contains (align vertically):* Number of guests:* tag:  ` div ` 
* classname:  ` max_guest ` 
* width: 100px
* fake text
* [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_group.png) 


* Number of bedrooms:* tag:  ` div ` 
* classname:  ` number_rooms ` 
* width: 100px
* fake text
* [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bed.png) 


* Number of bathrooms:* tag:  ` div ` 
* classname:  ` number_bathrooms ` 
* width: 100px
* fake text
* [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bath.png) 




* User section:* tag:  ` div ` 
* classname:  ` user ` 
* text  ` Owner: <fake text> ` 
*  ` Owner `  text should be in bold

* Description section:* tag:  ` div ` 
* classname:  ` description ` 

Requirements:
* You must use:  ` header ` ,  ` footer ` ,  ` section ` ,  ` article ` ,  ` button ` ,  ` h1 ` ,  ` h2 ` ,  ` h3 ` ,  ` h4 ` ,  ` ul ` ,  ` li `  tags
* No inline style
* You are not allowed to use the  ` img `  tag
* You are not allowed to use the  ` style `  tag in the  ` head `  tag
* All images must be stored in the  ` images `  folder
* You must have 5 CSS files:*  ` styles/4-common.css ` : for the global style (i.e.  ` body `  and  ` .container `  styles)
*  ` styles/3-header.css ` : for the header style
*  ` styles/3-footer.css ` : for the footer style
*  ` styles/6-filters.css ` : for the filters style
*  ` styles/8-places.css ` : for the places style

 ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2021/12/bd1088cbd5c50fd80b8f2027b88fc0b80b8c4d96.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220312%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220312T234944Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=aa64a67f29b28e19091c755d56c3a222c90d8d7791d0b31aa91af9bdabd947f6) 

 Task URLs  Github information Repo:
* GitHub repository:  ` AirBnB_clone ` 
* Directory:  ` web_static ` 
* File: ```bash
8-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/8-places.css, images/
```

 Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 4 advanced tasks now!](https://intranet.hbtn.io/projects/268/unlock_optionals) 

Ready for a  manual review