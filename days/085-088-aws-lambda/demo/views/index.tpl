<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.muicss.com/mui-0.9.41/css/mui.min.css" rel="stylesheet" type="text/css" />
    <script src="https://cdn.muicss.com/mui-0.9.41/js/mui.min.js"></script>
    <title>{{ title }}</title>
	<style>
		#code {
			font-size: 85%;
			border: 1px solid #ddd;
		}
		#pepOutput {
			margin-top: 15px;
		}
		#pepOutput, #code {
			height: 400px;
		}
		.feedback {
			height: 10px;
		}
		.ok {
			color: green;
		}
	</style>
  </head>
  <body>
    <div class="feedback mui--bg-primary"></div>
    <div class="mui-panel">
      <h1 class="mui--text-display1 mui--text-center">{{ title }}</h1>
      <h2 class="mui--text-body2 mui--text-center">Indeed, the ratio of time spent reading versus writing is well over 10 to 1. We are constantly reading old code as part of the effort to write new code. - Robert C. Martin</h2>
    </div>

  <div class="mui-row">

    <div class="mui-col-md-6">
		<form class="mui-form mui-container" id="pepForm" method="post">
		<div class="mui-textfield">
			<textarea id="code" name="code" placeholder="Paste your code here ...">{{ code }}</textarea>
		</div>
		<button type="submit" class="mui-btn mui-btn--primary">Verify code</button>
		</form>
	</div>

    <div class="mui-col-md-6">
		<div class="mui-container" id="pepOutput">
			%if code:
				%if pep_errors:
					<div class="feedback mui--bg-danger"></div>
					<pre>{{ pep_errors }}</pre>
				%else:
					<div class="feedback mui--bg-primary"></div>
					<strong class="ok">PEP8 Check OK</strong>
				%end
		</div>
	</div>

  </div>

  </body>
</html>
