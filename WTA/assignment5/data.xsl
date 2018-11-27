<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>My booklet Collection</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>Name</th>
      <th>Genre</th>
      <th>Place </th>
    </tr>
    <xsl:for-each select="booklet/concert_ad">
		<xsl:choose>
        <xsl:when test="@type = 'Pop'">
          <tr style="background-color:#cccc00">
            <td><xsl:value-of select="name"/></td>
            <td><xsl:value-of select="genre"/></td>
            <td><xsl:value-of select="place"/></td>
            
          </tr>
        </xsl:when>
        <xsl:when test="@type = 'Instrumental'">
          <tr style="background-color:#00cc00">
            <td><xsl:value-of select="name"/></td>
            <td><xsl:value-of select="genre"/></td>
            <td><xsl:value-of select="place"/></td>
          </tr>
        </xsl:when>
        <xsl:otherwise>
          <tr style="background-color:#cccccc">
 			<td><xsl:value-of select="name"/></td>
            <td><xsl:value-of select="genre"/></td>
            <td><xsl:value-of select="place"/></td>
          </tr>
        </xsl:otherwise>
      </xsl:choose>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet> 