#!/usr/bin/env python
# coding=utf-8
import glob


files = [f for f in glob.glob('../*.txt')]
titles = [f for f in glob.glob('../titles/*.txt')]
#print(titles)

header = '''
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>jQuery Mobile: Theme Download</title>
	<link rel="stylesheet" href="../themes/my.min.css" />
	<link rel="stylesheet" href="../themes/jquery.mobile.icons.min.css" />
	<link rel="stylesheet" href="../css/jquery.mobile.structure-1.4.5.min.css" />
	<script src="../js/jquery-1.11.1.min.js"></script>
	<script src="../js/jquery.mobile-1.4.5.min.js"></script>
</head>
<body>
	<div data-role="page" data-theme="a">
		<div data-role="header" data-position="inline">
			<h1 class="class-myfont">{title}</h1>
		</div>
		<div data-role="content" data-theme="a" class="class-myfont">
'''        

footer = '''
		</div>
        
        <div data-role="footer" data-theme="a" data-position="fixed" data-tap-toggle="false">		
            <div data-role="navbar">
                <ul>
                    <li><a onclick="window.location='../index.html'" data-rel="back" data-direction="reverse">Back</a></li>				
                </ul>
            </div>
        </div>         
        <!--
        <div data-role="header" data-position="inline">
            <a rel="external" href="../index.html"><p><strong>Back</strong></p></a>
		</div>
        -->
	</div>
    <script type="text/javascript" src="../cordova.js"></script>
    <script type="text/javascript" src="../js/index.js"></script>
</body>
</html>
'''


for ff, tt in zip(files, titles):
    file_name = '{}.html'.format(ff.split('/')[-1].split('.')[0])
    #title_name = '{}'.format(tt.split('/')[-1].split('.')[0])
    #print(file_name)
    with open('test/{}'.format(file_name), 'w') as f:
        f.write(header.format(title=open(tt).read()))
        f.write(open(ff).read())
        f.write(footer)

'''
for ff, tt in zip(files, titles):
    file_name = '{}.html'.format(ff.split('/')[-1].split('.')[0])
    title_name = '{}.html'.format(tt.split('/')[-1].split('.')[0])
    #print(file_name)
    with open(file_name, 'w') as f:
        f.write(header.format(title=open())
        f.write(open(ff).read())
        f.write(footer)
'''
